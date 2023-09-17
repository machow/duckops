from duckops.core.siuba import to_symbol, DuckdbColumn, ReplaceFx
from duckops.core.dispatch import dispatch_on_trait, create_generic
from duckops.core._type_backends import SbLazy
from duckops.core.data_style import IsSymbol, IsLiteral, IsConcrete
from duckops.core.sql import lambda_function, extract_infix, list_comprehension

from sqlalchemy import sql


def _raise_for_not_lazy(f):
    @f.register(IsLiteral)
    @f.register(IsConcrete)
    def raise_not_lazy(codata, *args, **kwargs):
        raise NotImplementedError(
            f"{f.__name__} currently requires using siuba lazy expressions (_)"
        )

    return f


# TODO: move lam into siuba -- accept it can only be used in verbs for now.
@_raise_for_not_lazy
@create_generic
def lam(expr):
    # TODO: shouldn't need a lam function, the duckdp ops
    # themselves should handle this
    raise NotImplementedError()


@lam.register
def _lam_lazy(codata: IsSymbol, expr: SbLazy):
    from siuba.siu import strip_symbolic

    new_expr = ReplaceFx(sql.column("x")).enter(strip_symbolic(expr))

    # TODO: wrap in Lazy
    return to_symbol(lam, (new_expr,))


@lam.register
def _lam_duckdb(codata: DuckdbColumn, expr):
    return lambda_function(sql.column("x"), expr)


@create_generic
def extract(obj, ii):
    # TODO: this won't work with literals, since there is no generic "extract"
    # in duckdb
    ...


@extract.register
def _extract_duckdb(codata: DuckdbColumn, obj, ii):
    return extract_infix(obj, ii)


@_raise_for_not_lazy
@create_generic
def list_comp(body, iterable, *ifs):
    # TODO ifs should not be *args, but we need to be
    # careful handling lists of calls in lazy expressions
    return dispatch_on_trait(list_comp, (body, iterable, *ifs), {})


@list_comp.register
def _list_comp_lazy(codata: IsSymbol, body, iterable, *ifs):
    replacer = ReplaceFx(sql.column("x"))
    new_body = replacer.visit(body)

    new_ifs = list(map(replacer.visit, ifs))

    return to_symbol(list_comp, (new_body, iterable, *new_ifs))


@list_comp.register
def _list_comp_sql(codata: DuckdbColumn, body, iterable, *ifs):
    return list_comprehension(body, iterable, *ifs)
