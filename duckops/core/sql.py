from sqlalchemy.sql.expression import FunctionElement
from sqlalchemy.ext.compiler import compiles


class assign_equals(FunctionElement):
    name = "assign_equals"
    inherit_cache = True


class lambda_function(FunctionElement):
    name = "lambda_function"
    inherit_cache = True


class list_comprehension(FunctionElement):
    # should be 3 entries: body, iterable, ifs
    name = "list_comprehension"
    inherit_cache = True


class extract_infix(FunctionElement):
    name = "extract_infix"
    inherit_cache = True


@compiles(assign_equals)
def _(element, compiler, **kw):
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs} := {proc_rhs}"


@compiles(extract_infix)
def _(element, compiler, **kw):
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs}[{proc_rhs}]"


@compiles(lambda_function)
def _(element, compiler, **kw):
    # lhs should be called parameter, rhs body
    lhs, rhs = element.clauses
    proc_lhs, proc_rhs = compiler.process(lhs, **kw), compiler.process(rhs, **kw)
    return f"{proc_lhs} -> {proc_rhs}"


@compiles(list_comprehension)
def _(element, compiler, **kw):
    # lhs should be called parameter, rhs body
    procs = [compiler.process(el, **kw) for el in element.clauses]
    iterable, body, *ifs = procs

    str_ifs = "IF ".join([" "] + ifs)
    return f"[{body} for x in {iterable}{str_ifs}]"
