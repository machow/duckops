from __future__ import annotations

from functools import wraps, singledispatch

# concrete data ---
from duckops.core.siuba import (  # noqa: F401
    ReplaceFx,
    sql_win,
    register_agg,
    flatten_arg_kwargs,
    NoArgOver,
    assign_equals,
    lambda_function,
    list_comprehension,
    extract_infix,
)
from siuba.siu.dispatchers import NoArgs
from siuba.sql.dialects.duckdb import DuckdbColumn

from duckops.core.convert import convert
from duckops.core.query_call import query_call
from duckops.prototypes import (  # noqa: F401
    PdSeries,
    PlSeries,
    DatetimeLike,
    StringLike,
    LiteralLike,
    IsLiteral,
    IsConcrete,
    IsConcretePandas,
    IsConcretePolars,
    IsSymbol,
    ConcreteLike,
    SymbolLike,
    data_style,
)
from sqlalchemy import sql


# Pre-processing steps ----
#   * process all LiteralLike to go into SQL
#   * ConcreteLike dispatch: separate literals and concretes
#   * Handle homogeneous tuples as LiteralLike list


def support_no_args(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        # Case 1: no arguments -----
        if not len(args):
            return f(NoArgs(), *args, **kwargs)

        return f(*args, **kwargs)

    return wrapped


def create_generic(_f):
    @support_no_args
    @singledispatch
    @wraps(_f)
    def f(*args, **kwargs):
        return dispatch_on_trait(f, args, kwargs)

    @f.register
    def _no_args(x: NoArgs, *args, **kwargs):
        # for functions like struct_pack that are all kwargs
        return dispatch_on_trait(f, args, kwargs)

    @f.register
    def _literal(codata: IsLiteral, *args, **kwargs):
        return query_call(codata, args, f, kwargs)

    @f.register
    def _concrete(codata: IsConcrete, *args):
        raise NotImplementedError()

    @f.register
    def _concrete_pd(codata: IsConcretePandas, *args):
        # TODO: support kwargs here
        return query_call(codata, args, f)

    @f.register
    def _concrete_pl(codata: IsConcretePolars, *args):
        # TODO: support kwargs here
        return query_call(codata, args, f)

    @f.register
    def _symbol(codata: IsSymbol, *args):
        # TODO: support kwargs here
        return to_symbol(f, args)

    @f.register
    def _duckdb_translate(codata: DuckdbColumn, *args, **kwargs):
        # TODO: grabbing __name__ inside this func feels a bit hacky
        named_args = [assign_equals(sql.text(k), v) for k, v in kwargs.items()]
        return getattr(sql.func, f.__name__)(*args, *named_args)

    # @_core.sql_agg("arg_max", _tr.AggOver)

    return f


def to_symbol(dispatcher, args):
    from siuba.siu import create_sym_call, FuncArg

    # TODO: need the dispatch for when it receives the column collection?
    converted = [convert(arg) if isinstance(arg, LiteralLike) else arg for arg in args]
    return create_sym_call(FuncArg(dispatcher), *converted)


@singledispatch
def lam(expr):
    # TODO: shouldn't need a lam function, the duckdp ops
    # themselves should handle this
    raise NotImplementedError()


@lam.register
def _lam_lazy(expr: SymbolLike):
    from siuba.siu import strip_symbolic

    new_expr = ReplaceFx(sql.column("x")).enter(strip_symbolic(expr))

    return to_symbol(lam, (new_expr,))


@lam.register
def _lam_duckdb(codata: DuckdbColumn, expr):
    return lambda_function(sql.column("x"), expr)


@create_generic
def extract(obj, ii):
    ...


@extract.register
def _extract_duckdb(codata: DuckdbColumn, obj, ii):
    return extract_infix(obj, ii)


@singledispatch
def list_comp(body, iterable, *ifs):
    # TODO ifs should not be *args, but we need to be
    # careful handling lists of calls in lazy expressions
    return dispatch_on_trait(list_comp, (body, iterable, *ifs), {})


@list_comp.register
def _list_comp(codata: IsSymbol, body, iterable, *ifs):
    replacer = ReplaceFx(sql.column("x"))
    new_body = replacer.visit(body)

    new_ifs = list(map(replacer.visit, ifs))

    return to_symbol(list_comp, (new_body, iterable, *new_ifs))


@list_comp.register
def _list_comp(codata: DuckdbColumn, body, iterable, *ifs):
    return list_comprehension(body, iterable, *ifs)


def dispatch_on_trait(dispatcher, args, kwargs):
    flat_args = flatten_arg_kwargs(args, kwargs)
    trait = dispatch_style(flat_args)

    # TODO: check if signature is in registry, and fail if not. Otherwise,
    # we will likely infinitely recurse
    return dispatcher(trait, *args, **kwargs)


def dispatch_style(args):
    concretes, literals, symbols = set(), set(), set()

    for arg in args:
        if isinstance(arg, ConcreteLike):
            concretes.add(type(arg))
        elif isinstance(arg, LiteralLike):
            # TODO: Interval is a Call and a Literal
            literals.add(type(arg))
        elif isinstance(arg, SymbolLike):
            symbols.add(type(arg))

    # guards ----
    if len(concretes) > 1:
        _types = "\n  *".join(map(str, concretes))
        raise NotImplementedError(
            "Mixing concrete types not allowed." f" Detected these concretes:\n{_types}"
        )

    # trait for dispatch ----
    if not args:
        return IsLiteral()
    elif symbols and concretes:
        raise NotImplementedError()
    elif symbols:
        # TODO: we have sets of types, but singledispatch only works with instances,
        # so we have to manually call its dispatch method (which takes types).
        return data_style.dispatch(list(symbols)[0])(None)
    elif concretes:
        # TODO: same as above :/
        return data_style.dispatch(list(concretes)[0])(None)
    elif literals:
        return IsLiteral()

    _types = "\n  * ".join([""] + [type(arg).__name__ for arg in args])
    raise TypeError(f"Cannot dispatch on this combination of types: \n{_types}")
