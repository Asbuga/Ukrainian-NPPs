import pytest

from notebook.utils.utils import get_date


def test_get_date_valid_quarter():
    assert get_date(year=2020, quarter=1) == "31.03.2020"
    assert get_date(year=2020, quarter=2) == "30.06.2020"
    assert get_date(year=2020, quarter=3) == "30.09.2020"
    assert get_date(year=2020, quarter=4) == "31.12.2020"


def test_get_date_invalid_quarter():
    with pytest.raises(ValueError, match="Quarter must be between 1 – 4."):
        get_date(2023, 0)
    with pytest.raises(ValueError, match="Quarter must be between 1 – 4."):
        get_date(2023, 5)
