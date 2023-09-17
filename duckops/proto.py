from __future__ import annotations

from functools import wraps, singledispatch

# concrete data ---
from siuba.sql.dialects.duckdb import DuckdbColumn
from duckops.core.siuba import to_symbol, register_agg  # noqa: F401

from duckops.core.sql import (
    assign_equals,
)

from duckops.core.query_call import query_call
from duckops.prototypes import (  # noqa: F401
    IsUnknown,
    IsLiteral,
    IsConcrete,
    IsConcretePandas,
    IsConcretePolars,
    IsSymbol,
    data_style,
)
from sqlalchemy import sql


# Pre-processing steps ----
#   * process all LiteralLike to go into SQL
#   * ConcreteLike dispatch: separate literals and concretes
#   * Handle homogeneous tuples as LiteralLike list
class NoArgs:
    """Represent a lack of positional arguments to a singledispatch call.

    This is necessary because functools.singledispatch requires at least
    one argument.
    """


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

    return f


def dispatch_on_trait(dispatcher, args, kwargs):
    flat_args = flatten_arg_kwargs(args, kwargs)
    trait = dispatch_style(flat_args)

    # TODO: check if signature is in registry, and fail if not. Otherwise,
    # we will likely infinitely recurse
    return dispatcher(trait, *args, **kwargs)


def flatten_arg_kwargs(args, kwargs):
    return (*args, *kwargs.values())


def dispatch_style(args):
    concretes, literals, symbols, unknown = set(), set(), set(), set()

    for arg in args:
        ds = data_style(arg)
        if isinstance(ds, IsConcrete):
            active = concretes
        elif isinstance(ds, IsLiteral):
            # TODO: Interval is a Call and a Literal
            active = literals
        elif isinstance(ds, IsSymbol):
            active = symbols
        elif isinstance(ds, IsUnknown):
            # note that unknown args are currently skipped over
            active = unknown
        else:
            raise TypeError(f"Unsupported type: {type(arg)}")

        active.add(type(ds))

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
        # TODO: we stored a set of trait types, but expect dispatch_style to return
        # an instance of the trait type. If traits defined a __hash__, we could work
        # around this.
        return list(symbols)[0]()
    elif concretes:
        # TODO: same as above :/
        return list(concretes)[0]()
    elif literals:
        return IsLiteral()

    _types = "\n  * ".join([""] + [type(arg).__name__ for arg in args])
    raise TypeError(f"Cannot dispatch on this combination of types: \n{_types}")
