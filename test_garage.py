import pytest
from garage import garage, garageOne, garageTwo, enter_garage, exit_garage, get_available_spots, calculate_fee

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

@pytest.mark.parametrize("garage, expected", [(garage, 7), (garageOne, 5), (garageTwo, 0)])
def test_available_spots(garage, expected):
    assert get_available_spots(garage) == expected

def test_calculate_fee_valid():
    assert calculate_fee(5, 10.0) == 50.0

def test_calculate_fee_invalid_hours():
    with pytest.raises(ValueError):
        calculate_fee(-5, 10.0)

def test_calculate_fee_invalid_rate():
    with pytest.raises(ValueError):
        calculate_fee(5, -10.0)

def test_calculate_fee_invalid_type():
    with pytest.raises(TypeError):
        calculate_fee(5, '10.0')