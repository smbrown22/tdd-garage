import pytest
from garage import enter_garage 

def test_enter_garage_successful_add():
    enter_garage(garage, car_id, entry_hour) 
    assert "12345" in garage 
