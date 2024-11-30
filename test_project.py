
import pytest
from project import (
    convert_area,
    convert_length,
    convert_temperature,
    convert_weight,
    convert_speed
)

def test_convert_area():

    assert convert_area(1000, 'square_meter', 'square_kilometer') == 1e-3
    assert convert_area(1, 'square_kilometer', 'square_meter') == 1e6
    assert convert_area(1, 'square_meter', 'square_foot') == 10.764
    assert convert_area(1, 'square_yard', 'square_mile') == 3.861e-7


def test_convert_length():

    assert convert_length(1000, 'meter', 'kilometer') == 1
    assert convert_length(1, 'kilometer', 'meter') == 1000
    assert convert_length(1, 'mile', 'meter') == 1609.34
    assert convert_length(1, 'yard', 'foot') == 3

def test_convert_temperature():

    assert convert_temperature(0, 'celsius', 'fahrenheit') == 32
    assert convert_temperature(32, 'fahrenheit', 'celsius') == 0
    assert convert_temperature(0, 'celsius', 'kelvin') == 273.15
    assert convert_temperature(273.15, 'kelvin', 'celsius') == 0
    assert convert_temperature(32, 'fahrenheit', 'kelvin') == 273.15
    assert convert_temperature(273.15, 'kelvin', 'fahrenheit') == 32


def test_convert_weight():

    assert convert_weight(1000, 'gram', 'kilogram') == 1
    assert convert_weight(1, 'kilogram', 'gram') == 1000
    assert convert_weight(1, 'pound', 'kilogram') == 0.453592
    assert convert_weight(1, 'ounce', 'gram') == 28.3495


def test_convert_speed():

    assert convert_speed(1, 'meter_per_second', 'kilometer_per_hour') == 3.6
    assert convert_speed(1, 'kilometer_per_hour', 'meter_per_second') == 1/3.6
    assert convert_speed(1, 'mile_per_hour', 'meter_per_second') == 0.44704
    assert convert_speed(1, 'foot_per_second', 'mile_per_hour') == 0.682
