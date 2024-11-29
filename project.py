def convert_area(value, from_unit, to_unit):
    area_units = {
        'square_meter': 1,
        'square_kilometer': 1e-6,
        'square_centimeter': 1e4,
        'square_mile': 3.861e-7,
        'square_yard': 1.195e1,
        'square_foot': 1.076e2
    }
    return value * area_units[from_unit] / area_units[to_unit]

def convert_length(value, from_unit, to_unit):
    length_units = {
        'meter': 1,
        'kilometer': 1e-3,
        'centimeter': 1e2,
        'millimeter': 1e3,
        'mile': 6.2137e-4,
        'yard': 1.0936,
        'foot': 3.2808
    }
    return value * length_units[from_unit] / length_units[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return value * 9/5 + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (value - 32) * 5/9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (value - 273.15) * 9/5 + 32
    else:
        return value  # If same units

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        'gram': 1,
        'kilogram': 1e-3,
        'milligram': 1e3,
        'pound': 2.20462e-3,
        'ounce': 3.5274e-2
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def convert_speed(value, from_unit, to_unit):
    speed_units = {
        'meter_per_second': 1,
        'kilometer_per_hour': 3.6,
        'mile_per_hour': 2.23694,
        'foot_per_second': 3.28084
    }
    return value * speed_units[from_unit] / speed_units[to_unit]

def main():
    print("Welcome to Unit Converter!")

    conversion_type = input("What type of conversion do you need? (area, length, temperature, weight, speed): ").lower()

    if conversion_type == "area":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (square_meter, square_kilometer, square_centimeter, square_mile, square_yard, square_foot): ").lower()
        to_unit = input("Enter the unit to convert to (square_meter, square_kilometer, square_centimeter, square_mile, square_yard, square_foot): ").lower()
        result = convert_area(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")

    elif conversion_type == "length":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (meter, kilometer, centimeter, millimeter, mile, yard, foot): ").lower()
        to_unit = input("Enter the unit to convert to (meter, kilometer, centimeter, millimeter, mile, yard, foot): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")

    elif conversion_type == "temperature":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("Enter the unit to convert to (celsius, fahrenheit, kelvin): ").lower()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")

    elif conversion_type == "weight":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (gram, kilogram, milligram, pound, ounce): ").lower()
        to_unit = input("Enter the unit to convert to (gram, kilogram, milligram, pound, ounce): ").lower()
        result = convert_weight(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")

    elif conversion_type == "speed":
        value = float(input("Enter the value to convert: "))
        from_unit = input("Enter the unit to convert from (meter_per_second, kilometer_per_hour, mile_per_hour, foot_per_second): ").lower()
        to_unit = input("Enter the unit to convert to (meter_per_second, kilometer_per_hour, mile_per_hour, foot_per_second): ").lower()
        result = convert_speed(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")

    else:
        print("Invalid conversion type. Please select one from area, length, temperature, weight, or speed.")

if __name__ == "__main__":
    main()
