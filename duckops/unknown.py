
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("enum_first")
def enum_first(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("enum_last")
def enum_last(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("enum_code")
def enum_code(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("enum_range")
def enum_range(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("enum_range_boundary")
def enum_range_boundary(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("constant_or_null")
def constant_or_null(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("current_query")
def current_query(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("current_database")
def current_database(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("stem")
def stem(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("current_localtime")
def current_localtime(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("combine")
def combine(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("finalize")
def finalize(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("json_extract_path_text")
def json_extract_path_text(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("json_extract_path")
def json_extract_path(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("excel_text")
def excel_text(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("text")
def text(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("flatten")
def flatten(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("bit_position")
def bit_position(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("set_bit")
def set_bit(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("get_bit")
def get_bit(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("split")
def split(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("translate")
def translate(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("md5_number_lower")
def md5_number_lower(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("md5_number_upper")
def md5_number_upper(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("md5_number")
def md5_number(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("not_ilike_escape")
def not_ilike_escape(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("ilike_escape")
def ilike_escape(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("mod")
def mod(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("divide")
def divide(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("multiply")
def multiply(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("subtract")
def subtract(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("add")
def add(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_scalar("exp")
def exp(codata: DuckdbColumn, *args):
    """nan"""



@_core.sql_agg("argmin", _tr.AggOver)
def argmin(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("argmax", _tr.AggOver)
def argmax(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("sum_no_overflow", _tr.AggOver)
def sum_no_overflow(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("count_star", _tr.AggOver)
def count_star(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("sem", _tr.AggOver)
def sem(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("covar_samp", _tr.AggOver)
def covar_samp(codata: DuckdbColumnAgg, *args):
    """nan"""



@_core.sql_agg("mean", _tr.AggOver)
def mean(codata: DuckdbColumnAgg, *args):
    """nan"""
