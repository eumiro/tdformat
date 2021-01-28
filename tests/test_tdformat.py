import pytest

from tdformat.tdformat import Td


@pytest.mark.parametrize("format_spec", [None, 0, 1, 1.2, {}, b""])
def test_wrong_format_type(format_spec):
    td = Td(seconds=123)
    with pytest.raises(TypeError):
        td.__format__(format_spec)


@pytest.mark.parametrize(
    "format_spec, seconds, result",
    [
        ("", 1, ""),
        ("a", 1, "a"),
        ("äßč™", 1, "äßč™"),
        ("{}", 1, "{}"),
        ("{H}", 1, "{H}"),
        ("\\x", 1, "\\x"),
        ("%%", 1, "%"),
        ("%%%%", 1, "%%"),
        ("%S", 0, "0"),
        ("%S", 0.00000001, "0"),
        ("%S", 1, "1"),
        ("%S", 11, "11"),
        ("%S", 1_234_567, "1234567"),
    ],
)
def test_timedelta(format_spec, seconds, result):
    assert Td(seconds=seconds).__format__(format_spec) == result
