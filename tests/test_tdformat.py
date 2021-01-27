import pytest

from tdformat import Td



@pytest.mark.parametrize("format_spec", [None, 0, 1, 1.2, {}])
def test_wrong_format_type(format_spec):
    td = Td(seconds=123)
    with pytest.raises(TypeError):
        td.__format__(format_spec)


def test_true():
    assert True
