import pytest

@pytest.mark.xfail(reason="Найден баг в приложении")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Найденный баг в приложении уже исправлен")
def test_without_bug():
    ...