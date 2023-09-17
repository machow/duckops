
from __future__ import annotations

from typing import overload, TYPE_CHECKING
from duckops.core.dispatch import create_generic, register_agg

if TYPE_CHECKING:
    from duckops.core.data_style import *
    AAA = 1

del TYPE_CHECKING


__all__ = (
    "array_extract",
    "array_slice",
    "ascii",
    "bar",
    "base64",
    "bit_length",
    "concat",
    "concat_ws",
    "contains",
    "editdist3",
    "format",
    "from_base64",
    "hamming",
    "hash",
    "instr",
    "jaccard",
    "jaro_similarity",
    "jaro_winkler_similarity",
    "lcase",
    "left",
    "left_grapheme",
    "length",
    "length_grapheme",
    "levenshtein",
    "like_escape",
    "list_element",
    "list_extract",
    "lower",
    "lpad",
    "ltrim",
    "md5",
    "mismatches",
    "nfc_normalize",
    "not_like_escape",
    "ord",
    "position",
    "prefix",
    "printf",
    "regexp_extract",
    "regexp_full_match",
    "regexp_matches",
    "regexp_replace",
    "regexp_split_to_array",
    "repeat",
    "replace",
    "reverse",
    "right",
    "right_grapheme",
    "rpad",
    "rtrim",
    "starts_with",
    "str_split",
    "str_split_regex",
    "string_split",
    "string_split_regex",
    "string_to_array",
    "strip_accents",
    "strlen",
    "strpos",
    "substr",
    "substring",
    "substring_grapheme",
    "suffix",
    "to_base64",
    "trim",
    "ucase",
    "unicode",
    "upper"
)


@overload
def array_extract(col0: StringLike, col1: NumberLike) -> StringLike: ...

@overload
def array_extract(col0: StructLike, col1: StringLike) -> Any: ...

@create_generic
def array_extract(col0: list[Any], col1: NumberLike) -> Any:
    """Extract a single character using a (1-based) index.

    | duckdb example | result |
    | -------------- | ------ |
    | array_extract('DuckDB', 2) | 'u' |


    """


@create_generic
def array_slice(col0: Any, col1: NumberLike, col2: NumberLike, *args: Any) -> Any:
    """Extract a string using slice conventions. NULLs are interpreted as the bounds of the string. Negative values are accepted.

    | duckdb example | result |
    | -------------- | ------ |
    | array_slice('DuckDB', 5, NULL) | 'DB' |


    """


@create_generic
def ascii(col0: StringLike) -> NumberLike:
    """Returns an integer that represents the Unicode code point of the first character of the string

    | duckdb example | result |
    | -------------- | ------ |
    | ascii('Ω') | 937 |


    """


@overload
def bar(col0: NumberLike, col1: NumberLike, col2: NumberLike) -> StringLike: ...

@create_generic
def bar(col0: NumberLike, col1: NumberLike, col2: NumberLike, col3: NumberLike) -> StringLike:
    """Draw a band whose width is proportional to (x - min) and equal to width characters when x = max. width defaults to 80.

    | duckdb example | result |
    | -------------- | ------ |
    | bar(5, 0, 20, 10) | ██▌ |


    """


@create_generic
def base64(col0: ABlob) -> StringLike:
    """Convert a blob to a base64 encoded string. Alias of to_base64.

    | duckdb example | result |
    | -------------- | ------ |
    | base64('A'::blob) | 'QQ==' |


    """


@overload
def bit_length(col0: ABit) -> NumberLike: ...

@create_generic
def bit_length(col0: StringLike) -> NumberLike:
    """Number of bits in a string.

    | duckdb example | result |
    | -------------- | ------ |
    | bit_length('abc') | 24 |


    """


@create_generic
def concat(col0: StringLike, *args: StringLike) -> StringLike:
    """Concatenate many strings together

    | duckdb example | result |
    | -------------- | ------ |
    | concat('Hello', ' ', 'World') | Hello World |


    """


@create_generic
def concat_ws(col0: StringLike, col1: StringLike, *args: StringLike) -> StringLike:
    """Concatenate strings together separated by the specified separator

    | duckdb example | result |
    | -------------- | ------ |
    | concat_ws(',', 'Banana', 'Apple', 'Melon') | Banana,Apple,Melon |


    """


@create_generic
def contains(col0: StringLike, col1: StringLike) -> ABool:
    """Return true if search_string is found within string

    | duckdb example | result |
    | -------------- | ------ |
    | contains('abc','a') | true |


    """


@create_generic
def editdist3(col0: StringLike, col1: StringLike) -> NumberLike:
    """Alias of levenshtein for SQLite compatibility. The minimum number of single-character edits (insertions, deletions or substitutions) required to change one string to the other. Different case is considered different.

    | duckdb example | result |
    | -------------- | ------ |
    | editdist3('duck','db') | 3.0 |


    """


@create_generic
def format(col0: StringLike, *args: Any) -> StringLike:
    """Formats a string using fmt syntax

    | duckdb example | result |
    | -------------- | ------ |
    | format('Benchmark "{}" took {} seconds', 'CSV', 42) | Benchmark "CSV" took 42 seconds |


    """


@create_generic
def from_base64(col0: StringLike) -> ABlob:
    """Convert a base64 encoded string to a character string.

    | duckdb example | result |
    | -------------- | ------ |
    | from_base64('QQ==') | 'A' |


    """


@create_generic
def hamming(col0: StringLike, col1: StringLike) -> NumberLike:
    """The number of positions with different characters for 2 strings of equal length. Different case is considered different.

    | duckdb example | result |
    | -------------- | ------ |
    | hamming('duck','luck') | 1.0 |


    """


@create_generic
def hash(col0: Any, *args: Any) -> NumberLike:
    """Returns an integer with the hash of the value

    | duckdb example | result |
    | -------------- | ------ |
    | hash('🦆') | 2595805878642663834 |


    """


@create_generic
def instr(col0: StringLike, col1: StringLike) -> NumberLike:
    """Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.

    | duckdb example | result |
    | -------------- | ------ |
    | instr('test test','es') | 2 |


    """


@create_generic
def jaccard(col0: StringLike, col1: StringLike) -> NumberLike:
    """The Jaccard similarity between two strings. Different case is considered different. Returns a number between 0 and 1.

    | duckdb example | result |
    | -------------- | ------ |
    | jaccard('duck','luck') | 0.6 |


    """


@create_generic
def jaro_similarity(col0: StringLike, col1: StringLike) -> NumberLike:
    """The Jaro similarity between two strings. Different case is considered different. Returns a number between 0 and 1.

    | duckdb example | result |
    | -------------- | ------ |
    | jaro_similarity('duck','duckdb') | 0.88 |


    """


@create_generic
def jaro_winkler_similarity(col0: StringLike, col1: StringLike) -> NumberLike:
    """The Jaro-Winkler similarity between two strings. Different case is considered different. Returns a number between 0 and 1.

    | duckdb example | result |
    | -------------- | ------ |
    | jaro_winkler_similarity('duck','duckdb') | 0.93 |


    """


@create_generic
def lcase(col0: StringLike) -> StringLike:
    """Alias of lower. Convert string to lower case

    | duckdb example | result |
    | -------------- | ------ |
    | lcase('Hello') | hello |


    """


@create_generic
def left(col0: StringLike, col1: NumberLike) -> StringLike:
    """Extract the left-most count characters

    | duckdb example | result |
    | -------------- | ------ |
    | left('Hello🦆', 2) | He |


    """


@create_generic
def left_grapheme(col0: StringLike, col1: NumberLike) -> StringLike:
    """Extract the left-most grapheme clusters

    | duckdb example | result |
    | -------------- | ------ |
    | left_grapheme('🤦🏼‍♂️🤦🏽‍♀️', 1) | 🤦🏼‍♂️ |


    """


@overload
def length(col0: ABit) -> NumberLike: ...

@overload
def length(col0: list[Any]) -> NumberLike: ...

@create_generic
def length(col0: StringLike) -> NumberLike:
    """Number of characters in string

    | duckdb example | result |
    | -------------- | ------ |
    | length('Hello🦆') | 6 |


    """


@create_generic
def length_grapheme(col0: StringLike) -> NumberLike:
    """Number of grapheme clusters in string

    | duckdb example | result |
    | -------------- | ------ |
    | length_grapheme('🤦🏼‍♂️🤦🏽‍♀️') | 2 |


    """


@create_generic
def levenshtein(col0: StringLike, col1: StringLike) -> NumberLike:
    """The minimum number of single-character edits (insertions, deletions or substitutions) required to change one string to the other. Different case is considered different.

    | duckdb example | result |
    | -------------- | ------ |
    | levenshtein('duck','db') | 3.0 |


    """


@create_generic
def like_escape(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool:
    """Returns true if the string matches the like_specifier (see Pattern Matching). escape_character is used to search for wildcard characters in the string.

    | duckdb example | result |
    | -------------- | ------ |
    | like_escape('a%c', 'a$%c', '$') | true |


    """


@overload
def list_element(col0: StringLike, col1: NumberLike) -> StringLike: ...

@create_generic
def list_element(col0: list[Any], col1: NumberLike) -> Any:
    """An alias for array_extract.

    | duckdb example | result |
    | -------------- | ------ |
    | list_element('DuckDB', 2) | 'u' |


    """


@overload
def list_extract(col0: StringLike, col1: NumberLike) -> StringLike: ...

@create_generic
def list_extract(col0: list[Any], col1: NumberLike) -> Any:
    """An alias for array_extract.

    | duckdb example | result |
    | -------------- | ------ |
    | list_extract('DuckDB', 2) | 'u' |


    """


@create_generic
def lower(col0: StringLike) -> StringLike:
    """Convert string to lower case

    | duckdb example | result |
    | -------------- | ------ |
    | lower('Hello') | hello |


    """


@create_generic
def lpad(col0: StringLike, col1: NumberLike, col2: StringLike) -> StringLike:
    """Pads the string with the character from the left until it has count characters

    | duckdb example | result |
    | -------------- | ------ |
    | lpad('hello', 10, '>') | >>>>>hello |


    """


@overload
def ltrim(col0: StringLike, col1: StringLike) -> StringLike: ...

@create_generic
def ltrim(col0: StringLike) -> StringLike:
    """Removes any spaces from the left side of the string

    | duckdb example | result |
    | -------------- | ------ |
    | ltrim('␣␣␣␣test␣␣') | test␣␣ |


    """


@create_generic
def md5(col0: StringLike) -> StringLike:
    """Returns the MD5 hash of the value

    | duckdb example | result |
    | -------------- | ------ |
    | md5('123') | '202cb962ac59075b964b07152d234b70' |


    """


@create_generic
def mismatches(col0: StringLike, col1: StringLike) -> NumberLike:
    """The number of positions with different characters for 2 strings of equal length. Different case is considered different.

    | duckdb example | result |
    | -------------- | ------ |
    | mismatches('duck','luck') | 1.0 |


    """


@create_generic
def nfc_normalize(col0: StringLike) -> StringLike:
    """Convert string to Unicode NFC normalized string. Useful for comparisons and ordering if text data is mixed between NFC normalized and not.

    | duckdb example | result |
    | -------------- | ------ |
    | nfc_normalize('ardèch') | arde`ch |


    """


@create_generic
def not_like_escape(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool:
    """Returns false if the string matches the like_specifier (see Pattern Matching). escape_character is used to search for wildcard characters in the string.

    | duckdb example | result |
    | -------------- | ------ |
    | like_escape('a%c', 'a$%c', '$') | true |


    """


@create_generic
def ord(col0: StringLike) -> NumberLike:
    """Return ASCII character code of the leftmost character in a string.

    | duckdb example | result |
    | -------------- | ------ |
    | ord('ü') | 252 |


    """


@create_generic
def position(col0: StringLike, col1: StringLike) -> NumberLike:
    """Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.

    | duckdb example | result |
    | -------------- | ------ |
    | position('b' in 'abc') | 2 |


    """


@create_generic
def prefix(col0: StringLike, col1: StringLike) -> ABool:
    """Return true if string starts with search_string.

    | duckdb example | result |
    | -------------- | ------ |
    | prefix('abc', 'ab') | true |


    """


@create_generic
def printf(col0: StringLike, *args: Any) -> StringLike:
    """Formats a string using printf syntax

    | duckdb example | result |
    | -------------- | ------ |
    | printf('Benchmark "%s" took %d seconds', 'CSV', 42) | Benchmark "CSV" took 42 seconds |


    """


@overload
def regexp_extract(col0: StringLike, col1: StringLike, col2: NumberLike) -> StringLike: ...

@overload
def regexp_extract(col0: StringLike, col1: StringLike, col2: NumberLike, col3: StringLike) -> StringLike: ...

@create_generic
def regexp_extract(col0: StringLike, col1: StringLike) -> StringLike:
    """Split the string along the regex and extract first occurrence of group

    | duckdb example | result |
    | -------------- | ------ |
    | regexp_extract('hello_world', '([a-z ]+)_?', 1) | hello |


    """


@overload
def regexp_full_match(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool: ...

@create_generic
def regexp_full_match(col0: StringLike, col1: StringLike) -> ABool:
    """Returns true if the entire string matches the regex (see Pattern Matching)

    | duckdb example | result |
    | -------------- | ------ |
    | regexp_full_match('anabanana', '(an)*') | false |


    """


@overload
def regexp_matches(col0: StringLike, col1: StringLike, col2: StringLike) -> ABool: ...

@create_generic
def regexp_matches(col0: StringLike, col1: StringLike) -> ABool:
    """Returns true if a part of string matches the regex (see Pattern Matching)

    | duckdb example | result |
    | -------------- | ------ |
    | regexp_matches('anabanana', '(an)*') | true |


    """


@overload
def regexp_replace(col0: StringLike, col1: StringLike, col2: StringLike, col3: StringLike) -> StringLike: ...

@create_generic
def regexp_replace(col0: StringLike, col1: StringLike, col2: StringLike) -> StringLike:
    """Replaces the first occurrence of regex with the replacement, use 'g' modifier to replace all occurrences instead (see Pattern Matching)

    | duckdb example | result |
    | -------------- | ------ |
    | select regexp_replace('hello', '[lo]', '-') | he-lo |


    """


@overload
def regexp_split_to_array(col0: StringLike, col1: StringLike, col2: StringLike) -> list[StringLike]: ...

@create_generic
def regexp_split_to_array(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Alias of string_split_regex. Splits the string along the regex

    | duckdb example | result |
    | -------------- | ------ |
    | regexp_split_to_array('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |


    """


@create_generic
def repeat(col0: StringLike, col1: NumberLike) -> StringLike:
    """Repeats the string count number of times

    | duckdb example | result |
    | -------------- | ------ |
    | repeat('A', 5) | AAAAA |


    """


@create_generic
def replace(col0: StringLike, col1: StringLike, col2: StringLike) -> StringLike:
    """Replaces any occurrences of the source with target in string

    | duckdb example | result |
    | -------------- | ------ |
    | replace('hello', 'l', '-') | he--o |


    """


@create_generic
def reverse(col0: StringLike) -> StringLike:
    """Reverses the string

    | duckdb example | result |
    | -------------- | ------ |
    | reverse('hello') | olleh |


    """


@create_generic
def right(col0: StringLike, col1: NumberLike) -> StringLike:
    """Extract the right-most count characters

    | duckdb example | result |
    | -------------- | ------ |
    | right('Hello🦆', 3) | lo🦆 |


    """


@create_generic
def right_grapheme(col0: StringLike, col1: NumberLike) -> StringLike:
    """Extract the right-most count grapheme clusters

    | duckdb example | result |
    | -------------- | ------ |
    | right_grapheme('🤦🏼‍♂️🤦🏽‍♀️', 1) | 🤦🏽‍♀️ |


    """


@create_generic
def rpad(col0: StringLike, col1: NumberLike, col2: StringLike) -> StringLike:
    """Pads the string with the character from the right until it has count characters

    | duckdb example | result |
    | -------------- | ------ |
    | rpad('hello', 10, '<') | hello<<<<< |


    """


@overload
def rtrim(col0: StringLike, col1: StringLike) -> StringLike: ...

@create_generic
def rtrim(col0: StringLike) -> StringLike:
    """Removes any spaces from the right side of the string

    | duckdb example | result |
    | -------------- | ------ |
    | rtrim('␣␣␣␣test␣␣') | ␣␣␣␣test |


    """


@create_generic
def starts_with(col0: StringLike, col1: StringLike) -> ABool:
    """Return true if string begins with search_string

    | duckdb example | result |
    | -------------- | ------ |
    | starts_with('abc','a') | true |


    """


@create_generic
def str_split(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Alias of string_split. Splits the string along the separator

    | duckdb example | result |
    | -------------- | ------ |
    | str_split('hello␣world', '␣') | ['hello', 'world'] |


    """


@overload
def str_split_regex(col0: StringLike, col1: StringLike, col2: StringLike) -> list[StringLike]: ...

@create_generic
def str_split_regex(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Alias of string_split_regex. Splits the string along the regex

    | duckdb example | result |
    | -------------- | ------ |
    | str_split_regex('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |


    """


@create_generic
def string_split(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Splits the string along the separator

    | duckdb example | result |
    | -------------- | ------ |
    | string_split('hello␣world', '␣') | ['hello', 'world'] |


    """


@overload
def string_split_regex(col0: StringLike, col1: StringLike, col2: StringLike) -> list[StringLike]: ...

@create_generic
def string_split_regex(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Splits the string along the regex

    | duckdb example | result |
    | -------------- | ------ |
    | string_split_regex('hello␣world; 42', ';?␣') | ['hello', 'world', '42'] |


    """


@create_generic
def string_to_array(col0: StringLike, col1: StringLike) -> list[StringLike]:
    """Alias of string_split. Splits the string along the separator

    | duckdb example | result |
    | -------------- | ------ |
    | string_to_array('hello␣world', '␣') | ['hello', 'world'] |


    """


@create_generic
def strip_accents(col0: StringLike) -> StringLike:
    """Strips accents from string

    | duckdb example | result |
    | -------------- | ------ |
    | strip_accents('mühleisen') | muhleisen |


    """


@create_generic
def strlen(col0: StringLike) -> NumberLike:
    """Number of bytes in string

    | duckdb example | result |
    | -------------- | ------ |
    | strlen('🦆') | 4 |


    """


@create_generic
def strpos(col0: StringLike, col1: StringLike) -> NumberLike:
    """Alias of instr. Return location of first occurrence of search_string in string, counting from 1. Returns 0 if no match found.

    | duckdb example | result |
    | -------------- | ------ |
    | strpos('test test','es') | 2 |


    """


@overload
def substr(col0: StringLike, col1: NumberLike) -> StringLike: ...

@create_generic
def substr(col0: StringLike, col1: NumberLike, col2: NumberLike) -> StringLike:
    """Alias of substring. Extract substring of length characters starting from character start. Note that a start value of 1 refers to the first character of the string.

    | duckdb example | result |
    | -------------- | ------ |
    | substr('Hello', 2, 2) | el |


    """


@overload
def substring(col0: StringLike, col1: NumberLike) -> StringLike: ...

@create_generic
def substring(col0: StringLike, col1: NumberLike, col2: NumberLike) -> StringLike:
    """Extract substring of length characters starting from character start. Note that a start value of 1 refers to the first character of the string.

    | duckdb example | result |
    | -------------- | ------ |
    | substring('Hello', 2, 2) | el |


    """


@overload
def substring_grapheme(col0: StringLike, col1: NumberLike) -> StringLike: ...

@create_generic
def substring_grapheme(col0: StringLike, col1: NumberLike, col2: NumberLike) -> StringLike:
    """Extract substring of length grapheme clusters starting from character start. Note that a start value of 1 refers to the first character of the string.

    | duckdb example | result |
    | -------------- | ------ |
    | substring_grapheme('🦆🤦🏼‍♂️🤦🏽‍♀️🦆', 3, 2) | 🤦🏽‍♀️🦆 |


    """


@create_generic
def suffix(col0: StringLike, col1: StringLike) -> ABool:
    """Return true if string ends with search_string.

    | duckdb example | result |
    | -------------- | ------ |
    | suffix('abc', 'bc') | true |


    """


@create_generic
def to_base64(col0: ABlob) -> StringLike:
    """Convert a blob to a base64 encoded string. Alias of base64.

    | duckdb example | result |
    | -------------- | ------ |
    | to_base64('A'::blob) | QQ== |


    """


@overload
def trim(col0: StringLike, col1: StringLike) -> StringLike: ...

@create_generic
def trim(col0: StringLike) -> StringLike:
    """Removes any spaces from either side of the string

    | duckdb example | result |
    | -------------- | ------ |
    | trim('␣␣␣␣test␣␣') | test |


    """


@create_generic
def ucase(col0: StringLike) -> StringLike:
    """Alias of upper. Convert string to upper case

    | duckdb example | result |
    | -------------- | ------ |
    | ucase('Hello') | HELLO |


    """


@create_generic
def unicode(col0: StringLike) -> NumberLike:
    """Returns the unicode code of the first character of the string

    | duckdb example | result |
    | -------------- | ------ |
    | unicode('ü') | 252 |


    """


@create_generic
def upper(col0: StringLike) -> StringLike:
    """Convert string to upper case

    | duckdb example | result |
    | -------------- | ------ |
    | upper('Hello') | HELLO |


    """