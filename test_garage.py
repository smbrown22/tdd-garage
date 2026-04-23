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

def test_enter_garage_entry_hour_type():
    with pytest.raises(TypeError):
        enter_garage(garage, "23456", "8")

def test_exit_garage_successful_add():
    exit_garage(garage, "40000", 10) 
    assert "40000" not in garage

def test_exit_garage_doesnt_exist():
    with pytest.raises(KeyError):
        exit_garage(garage, "30000", 9)

