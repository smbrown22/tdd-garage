import pytest
from garage import garage, enter_garage 

def test_enter_garage_successful_add():

    enter_garage(garage, "12345", 8) 
    assert "12345" in garage 
