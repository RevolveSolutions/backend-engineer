import pytest
from main import Revolve

revolve = Revolve()

def test_total_number_of_days():
    result = revolve.total_days("flights.csv")
    assert result == 365

def test_departure_cities():
    result = revolve.departure_cities("flights.csv", "airports.csv")
    assert result == ['New York', 'Newark']

def test_relation():
    result = revolve.relation("flights.csv", "planes.csv")
    assert result == ['tailnum', 'year']

def test_manufacturer_with_most_delays():
    result = revolve.most_delay_manufacturer("flights.csv", "planes.csv")
    assert result == "EMBRAER"

def test_two_most_connected_cities():
    result = revolve.most_connected_cities("flights.csv", "airports.csv")
    assert result == ["New York", "Los Angeles"]

'''
# Output

PS C:\Users\Acer\OneDrive\Desktop\Revolve-Solutions\backend-engineer\data> pytest test.py
============================================================ test session starts ============================================================ 
platform win32 -- Python 3.9.6, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
rootdir: C:\Users\Acer\OneDrive\Desktop\Revolve-Solutions\backend-engineer\data
plugins: anyio-3.2.1
collected 5 items                                                                                                                             

test.py .....                                                                          [100%] 

============================================================ 5 passed in 12.06s ============================================================= 
'''