import pytest

from pydantic_ai_mcp_experiment.data import CityLocation


def test_instantiation_failure():
    with pytest.raises(ValueError):
        location = CityLocation()  # type: ignore


def test_instantiation_success():
    location = CityLocation(city="Berlin", country="Germany")

    assert isinstance(location, CityLocation)
    assert hasattr(location, "city")
    assert hasattr(location, "country")
    assert location.city == "Berlin"
    assert location.country == "Germany"
