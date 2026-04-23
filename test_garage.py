import pytest
from garage import garage, enter_garage 

def test_enter_garage_successful_add():
    enter_garage(garage, "12345", 8) 
    assert "12345" in garage 

def test_enter_garage_full_capacity():
    with pytest.raises(ValueError):
        enter_garage(garage, "54321", 10)

def test_enter_garage_car_exists():
    with pytest.raises(ValueError):
        enter_garage(garage, "12345", 8)

def 