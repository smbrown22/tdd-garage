garage = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
}

garageOne = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
}

garageTwo = {
    "capacity": 10,   # total number of spots
    "cars": {}         # car_id -> entry_hour (int)
}

def enter_garage(garage, car_id, entry_hour):
    if car_id in garage.get("cars"):
        raise ValueError
    elif len(garage) == garage.get("capacity"):
        raise ValueError 
    elif not isinstance(entry_hour, int):
        raise TypeError
    else:
        garage.get("capacity") == garage.get("capacity") - 1 
        

def exit_garage(garage, car_id):
    pass 

def get_available_spots(garage):
    return garage.get(capacity)  

def calculate_fee(hours, rate):
    if hours < 0 or rate < 0:
        raise ValueError
    elif not isinstance(hours , (int, float)) or not isinstance(rate, (int, float)):
        raise TypeError
    else:
        return hours * rate 
