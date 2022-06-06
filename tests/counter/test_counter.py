import pytest
from src.counter import count_ocurrences


def test_counter():
    assert count_ocurrences("tests/counter/languages.txt", "python") == 2
    assert count_ocurrences("tests/counter/languages.txt", "javascript") == 2
    assert count_ocurrences("tests/counter/languages.txt", "rust") == 1
    try:
        count_ocurrences("tests/counter/languages.txt", 5)
    except AttributeError:
        pytest.mark.xfail()
