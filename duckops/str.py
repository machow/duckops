
from . import _core
from siuba.sql import translate as _tr
from siuba.sql.dialects.duckdb import DuckdbColumn, DuckdbColumnAgg

@_core.sql_scalar("to_base64")
def to_base64(codata: DuckdbColumn, *args):
    """Convert a blob to a base64 encoded string. Alias of base64.
| duckdb example | result |
| -------------- | ------ |
| to_base64('A'::blob) | QQ== |
"""



@_core.sql_scalar("hash")
def hash(codata: DuckdbColumn, *args):
    """Returns an integer with the hash of the value
| duckdb example | result |
| -------------- | ------ |
| hash('🦆') | 2595805878642663834 |
"""



@_core.sql_scalar("array_extract")
def array_extract(codata: DuckdbColumn, *args):
    """Extract a single character using a (1-based) index.
| duckdb example | result |
| -------------- | ------ |
| array_extract('DuckDB', 2) | 'u' |
"""



@_core.sql_scalar("list_element")
def list_element(codata: DuckdbColumn, *args):
    """An alias for array_extract.
| duckdb example | result |
| -------------- | ------ |
| list_element('DuckDB', 2) | 'u' |
"""



@_core.sql_scalar("list_extract")
def list_extract(codata: DuckdbColumn, *args):
    """An alias for array_extract.
| duckdb example | result |
| -------------- | ------ |
| list_extract('DuckDB', 2) | 'u' |
"""



@_core.sql_scalar("array_slice")
def array_slice(codata: DuckdbColumn, *args):
    """Extract a string using slice conventions. NULLs are interpreted as the bounds of the string. Negative values are accepted.
| duckdb example | result |
| -------------- | ------ |
| array_slice('DuckDB', 5, NULL) | 'DB' |
"""



@_core.sql_scalar("from_base64")
def from_base64(codata: DuckdbColumn, *args):
    """Convert a base64 encoded string to a character string.
| duckdb example | result |
| -------------- | ------ |
| from_base64('QQ==') | 'A' |
"""



@_core.sql_scalar("base64")
def base64(codata: DuckdbColumn, *args):
    """Convert a blob to a base64 encoded string. Alias of to_base64.
| duckdb example | result |
| -------------- | ------ |
| base64('A'::blob) | 'QQ==' |
"""



@_core.sql_scalar("jaro_winkler_similarity")
def jaro_winkler_similarity(codata: DuckdbColumn, *args):
    """The Jaro-Winkler similarity between two strings. Different case is considered different. Returns a number between 0 and 1.
| duckdb example | result |
| -------------- | ------ |
| jaro_winkler_similarity('duck','duckdb') | 0.93 |
"""



@_core.sql_scalar("jaro_similarity")
def jaro_similarity(codata: DuckdbColumn, *args):
    """The Jaro similarity between two strings. Different case is considered different. Returns a number between 0 and 1.
| duckdb example | result |
| -------------- | ------ |
| jaro_similarity('duck','duckdb') | 0.88 |
"""



@_core.sql_scalar("jaccard")
def jaccard(codata: DuckdbColumn, *args):
    """The Jaccard similarity between two strings. Different case is considered different. Returns a number between 0 and 1.
| duckdb example | result |
| -------------- | ------ |
| jaccard('duck','luck') | 0.6 |
"""



@_core.sql_scalar("editdist3")
def editdist3(codata: DuckdbColumn, *args):
    """Alias of levenshtein for SQLite compatibility. The minimum number of single-character edits (insertions, deletions or substitutions) required to change one string to the other. Different case is considered different.
| duckdb example | result |
| -------------- | ------ |
| editdist3('duck','db') | 3.0 |
"""



@_core.sql_scalar("levenshtein")
def levenshtein(codata: DuckdbColumn, *args):
    """The minimum number of single-character edits (insertions, deletions or substitutions) required to change one string to the other. Different case is considered different.
| duckdb example | result |
| -------------- | ------ |
| levenshtein('duck','db') | 3.0 |
"""



@_core.sql_scalar("hamming")
def hamming(codata: DuckdbColumn, *args):
    """The number of positions with different characters for 2 strings of equal length. Different case is considered different.
| duckdb example | result |
| -------------- | ------ |
| hamming('duck','luck') | 1.0 |
"""



@_core.sql_scalar("mismatches")
def mismatches(codata: DuckdbColumn, *args):
    """The number of positions with different characters for 2 strings of equal length. Different case is considered different.
| duckdb example | result |
| -------------- | ------ |
| mismatches('duck','luck') | 1.0 |
"""



@_core.sql_scalar("ascii")
def ascii(codata: DuckdbColumn, *args):
    """Returns an integer that represents the Unicode code point of the first character of the string
| duckdb example | result |
| -------------- | ------ |
| ascii('Ω') | 937 |
"""



@_core.sql_scalar("bar")
def bar(codata: DuckdbColumn, *args):
    """Draw a band whose width is proportional to (x - min) and equal to width characters when x = max. width defaults to 80.
| duckdb example | result |
| -------------- | ------ |
| bar(5, 0, 20, 10) | ██▌ |
"""



@_core.sql_scalar("regexp_split_to_array")
def regexp_split_to_array(codata: DuckdbColumn, *args):
    """Alias of string_split_regex. Splits the string along the regex
| duckdb example | result |
| -------------- | ------ |
| regexp_split_to_array('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |
"""



@_core.sql_scalar("str_split_regex")
def str_split_regex(codata: DuckdbColumn, *args):
    """Alias of string_split_regex. Splits the string along the regex
| duckdb example | result |
| -------------- | ------ |
| str_split_regex('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |
"""



@_core.sql_scalar("string_split_regex")
def string_split_regex(codata: DuckdbColumn, *args):
    """Splits the string along the regex
| duckdb example | result |
| -------------- | ------ |
| string_split_regex('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |
"""



@_core.sql_scalar("string_to_array")
def string_to_array(codata: DuckdbColumn, *args):
    """Alias of string_split. Splits the string along the separator
| duckdb example | result |
| -------------- | ------ |
| string_to_array('hello␣world', '␣') | ['hello', 'world'] |
"""



@_core.sql_scalar("str_split")
def str_split(codata: DuckdbColumn, *args):
    """Alias of string_split. Splits the string along the separator
| duckdb example | result |
| -------------- | ------ |
| str_split('hello␣world', '␣') | ['hello', 'world'] |
"""



@_core.sql_scalar("string_split")
def string_split(codata: DuckdbColumn, *args):
    """Splits the string along the separator
| duckdb example | result |
| -------------- | ------ |
| string_split('hello␣world', '␣') | ['hello', 'world'] |
"""



@_core.sql_scalar("nfc_normalize")
def nfc_normalize(codata: DuckdbColumn, *args):
    """Convert string to Unicode NFC normalized string. Useful for comparisons and ordering if text data is mixed between NFC normalized and not.
| duckdb example | result |
| -------------- | ------ |
| nfc_normalize('ardèch') | arde`ch |
"""



@_core.sql_scalar("ord")
def ord(codata: DuckdbColumn, *args):
    """Return ASCII character code of the leftmost character in a string.
| duckdb example | result |
| -------------- | ------ |
| ord('ü') | 252 |
"""



@_core.sql_scalar("unicode")
def unicode(codata: DuckdbColumn, *args):
    """Returns the unicode code of the first character of the string
| duckdb example | result |
| -------------- | ------ |
| unicode('ü') | 252 |
"""



@_core.sql_scalar("trim")
def trim(codata: DuckdbColumn, *args):
    """Removes any spaces from either side of the string
| duckdb example | result |
| -------------- | ------ |
| trim('␣␣␣␣test␣␣') | test |
"""



@_core.sql_scalar("rtrim")
def rtrim(codata: DuckdbColumn, *args):
    """Removes any spaces from the right side of the string
| duckdb example | result |
| -------------- | ------ |
| rtrim('␣␣␣␣test␣␣') | ␣␣␣␣test |
"""



@_core.sql_scalar("ltrim")
def ltrim(codata: DuckdbColumn, *args):
    """Removes any spaces from the left side of the string
| duckdb example | result |
| -------------- | ------ |
| ltrim('␣␣␣␣test␣␣') | test␣␣ |
"""



@_core.sql_scalar("suffix")
def suffix(codata: DuckdbColumn, *args):
    """Return true if string ends with search_string.
| duckdb example | result |
| -------------- | ------ |
| suffix('abc', 'bc') | true |
"""



@_core.sql_scalar("rpad")
def rpad(codata: DuckdbColumn, *args):
    """Pads the string with the character from the right until it has count characters
| duckdb example | result |
| -------------- | ------ |
| rpad('hello', 10, '<') | hello<<<<< |
"""



@_core.sql_scalar("replace")
def replace(codata: DuckdbColumn, *args):
    """Replaces any occurrences of the source with target in string
| duckdb example | result |
| -------------- | ------ |
| replace('hello', 'l', '-') | he--o |
"""



@_core.sql_scalar("prefix")
def prefix(codata: DuckdbColumn, *args):
    """Return true if string starts with search_string.
| duckdb example | result |
| -------------- | ------ |
| prefix('abc', 'ab') | true |
"""



@_core.sql_scalar("position")
def position(codata: DuckdbColumn, *args):
    """Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.
| duckdb example | result |
| -------------- | ------ |
| position('b' in 'abc') | 2 |
"""



@_core.sql_scalar("strpos")
def strpos(codata: DuckdbColumn, *args):
    """Alias of instr. Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.
| duckdb example | result |
| -------------- | ------ |
| strpos('test test','es') | 2 |
"""



@_core.sql_scalar("instr")
def instr(codata: DuckdbColumn, *args):
    """Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.
| duckdb example | result |
| -------------- | ------ |
| instr('test test','es') | 2 |
"""



@_core.sql_scalar("substring_grapheme")
def substring_grapheme(codata: DuckdbColumn, *args):
    """Extract substring of length grapheme clusters starting from character start. Note that a start value of 1 refers to the first character of the string.
| duckdb example | result |
| -------------- | ------ |
| substring_grapheme('🦆🤦🏼‍♂️🤦🏽‍♀️🦆', 3, 2) | 🤦🏽‍♀️🦆 |
"""



@_core.sql_scalar("substr")
def substr(codata: DuckdbColumn, *args):
    """Alias of substring. Extract substring of length characters starting from character start. Note that a start value of 1 refers to the first character of the string.
| duckdb example | result |
| -------------- | ------ |
| substr('Hello', 2, 2) | el |
"""



@_core.sql_scalar("substring")
def substring(codata: DuckdbColumn, *args):
    """Extract substring of length characters starting from character start. Note that a start value of 1 refers to the first character of the string.
| duckdb example | result |
| -------------- | ------ |
| substring('Hello', 2, 2) | el |
"""



@_core.sql_scalar("regexp_extract")
def regexp_extract(codata: DuckdbColumn, *args):
    """Split the string along the regex and extract first occurrence of group
| duckdb example | result |
| -------------- | ------ |
| regexp_extract('hello_world', '([a-z ]+)_?', 1) | hello |
"""



@_core.sql_scalar("regexp_replace")
def regexp_replace(codata: DuckdbColumn, *args):
    """Replaces the first occurrence of regex with the replacement, use 'g' modifier to replace all occurrences instead (see Pattern Matching)
| duckdb example | result |
| -------------- | ------ |
| select regexp_replace('hello', '[lo]', '-') | he-lo |
"""



@_core.sql_scalar("regexp_matches")
def regexp_matches(codata: DuckdbColumn, *args):
    """Returns true if a part of string matches the regex (see Pattern Matching)
| duckdb example | result |
| -------------- | ------ |
| regexp_matches('anabanana', '(an)*') | true |
"""



@_core.sql_scalar("regexp_full_match")
def regexp_full_match(codata: DuckdbColumn, *args):
    """Returns true if the entire string matches the regex (see Pattern Matching)
| duckdb example | result |
| -------------- | ------ |
| regexp_full_match('anabanana', '(an)*') | false |
"""



@_core.sql_scalar("format")
def format(codata: DuckdbColumn, *args):
    """Formats a string using fmt syntax
| duckdb example | result |
| -------------- | ------ |
| format('Benchmark "{}" took {} seconds', 'CSV', 42) | Benchmark "CSV" took 42 seconds |
"""



@_core.sql_scalar("printf")
def printf(codata: DuckdbColumn, *args):
    """Formats a string using printf syntax
| duckdb example | result |
| -------------- | ------ |
| printf('Benchmark "%s" took %d seconds', 'CSV', 42) | Benchmark "CSV" took 42 seconds |
"""



@_core.sql_scalar("right_grapheme")
def right_grapheme(codata: DuckdbColumn, *args):
    """Extract the right-most count grapheme clusters
| duckdb example | result |
| -------------- | ------ |
| right_grapheme('🤦🏼‍♂️🤦🏽‍♀️', 1) | 🤦🏽‍♀️ |
"""



@_core.sql_scalar("right")
def right(codata: DuckdbColumn, *args):
    """Extract the right-most count characters
| duckdb example | result |
| -------------- | ------ |
| right('Hello🦆', 3) | lo🦆 |
"""



@_core.sql_scalar("md5")
def md5(codata: DuckdbColumn, *args):
    """Returns the MD5 hash of the value
| duckdb example | result |
| -------------- | ------ |
| md5('123') | '202cb962ac59075b964b07152d234b70' |
"""



@_core.sql_scalar("left_grapheme")
def left_grapheme(codata: DuckdbColumn, *args):
    """Extract the left-most grapheme clusters
| duckdb example | result |
| -------------- | ------ |
| left_grapheme('🤦🏼‍♂️🤦🏽‍♀️', 1) | 🤦🏼‍♂️ |
"""



@_core.sql_scalar("left")
def left(codata: DuckdbColumn, *args):
    """Extract the left-most count characters
| duckdb example | result |
| -------------- | ------ |
| left('Hello🦆', 2) | He |
"""



@_core.sql_scalar("lpad")
def lpad(codata: DuckdbColumn, *args):
    """Pads the string with the character from the left until it has count characters
| duckdb example | result |
| -------------- | ------ |
| lpad('hello', 10, '>') | >>>>>hello |
"""



@_core.sql_scalar("not_like_escape")
def not_like_escape(codata: DuckdbColumn, *args):
    """Returns false if the string matches the like_specifier (see Pattern Matching). escape_character is used to search for wildcard characters in the string.
| duckdb example | result |
| -------------- | ------ |
| like_escape('a%c', 'a$%c', '$') | true |
"""



@_core.sql_scalar("like_escape")
def like_escape(codata: DuckdbColumn, *args):
    """Returns true if the string matches the like_specifier (see Pattern Matching). escape_character is used to search for wildcard characters in the string.
| duckdb example | result |
| -------------- | ------ |
| like_escape('a%c', 'a$%c', '$') | true |
"""



@_core.sql_scalar("bit_length")
def bit_length(codata: DuckdbColumn, *args):
    """Number of bits in a string.
| duckdb example | result |
| -------------- | ------ |
| bit_length('abc') | 24 |
"""



@_core.sql_scalar("strlen")
def strlen(codata: DuckdbColumn, *args):
    """Number of bytes in string
| duckdb example | result |
| -------------- | ------ |
| strlen('🦆') | 4 |
"""



@_core.sql_scalar("length_grapheme")
def length_grapheme(codata: DuckdbColumn, *args):
    """Number of grapheme clusters in string
| duckdb example | result |
| -------------- | ------ |
| length_grapheme('🤦🏼‍♂️🤦🏽‍♀️') | 2 |
"""



@_core.sql_scalar("length")
def length(codata: DuckdbColumn, *args):
    """Number of characters in string
| duckdb example | result |
| -------------- | ------ |
| length('Hello🦆') | 6 |
"""



@_core.sql_scalar("contains")
def contains(codata: DuckdbColumn, *args):
    """Return true if search_string is found within string
| duckdb example | result |
| -------------- | ------ |
| contains('abc','a') | true |
"""



@_core.sql_scalar("starts_with")
def starts_with(codata: DuckdbColumn, *args):
    """Return true if string begins with search_string
| duckdb example | result |
| -------------- | ------ |
| starts_with('abc','a') | true |
"""



@_core.sql_scalar("concat_ws")
def concat_ws(codata: DuckdbColumn, *args):
    """Concatenate strings together separated by the specified separator
| duckdb example | result |
| -------------- | ------ |
| concat_ws(',', 'Banana', 'Apple', 'Melon') | Banana,Apple,Melon |
"""



@_core.sql_scalar("concat")
def concat(codata: DuckdbColumn, *args):
    """Concatenate many strings together
| duckdb example | result |
| -------------- | ------ |
| concat('Hello', ' ', 'World') | Hello World |
"""



@_core.sql_scalar("strip_accents")
def strip_accents(codata: DuckdbColumn, *args):
    """Strips accents from string
| duckdb example | result |
| -------------- | ------ |
| strip_accents('mühleisen') | muhleisen |
"""



@_core.sql_scalar("ucase")
def ucase(codata: DuckdbColumn, *args):
    """Alias of upper. Convert string to upper case
| duckdb example | result |
| -------------- | ------ |
| ucase('Hello') | HELLO |
"""



@_core.sql_scalar("upper")
def upper(codata: DuckdbColumn, *args):
    """Convert string to upper case
| duckdb example | result |
| -------------- | ------ |
| upper('Hello') | HELLO |
"""



@_core.sql_scalar("lcase")
def lcase(codata: DuckdbColumn, *args):
    """Alias of lower. Convert string to lower case
| duckdb example | result |
| -------------- | ------ |
| lcase('Hello') | hello |
"""



@_core.sql_scalar("lower")
def lower(codata: DuckdbColumn, *args):
    """Convert string to lower case
| duckdb example | result |
| -------------- | ------ |
| lower('Hello') | hello |
"""



@_core.sql_scalar("reverse")
def reverse(codata: DuckdbColumn, *args):
    """Reverses the string
| duckdb example | result |
| -------------- | ------ |
| reverse('hello') | olleh |
"""
