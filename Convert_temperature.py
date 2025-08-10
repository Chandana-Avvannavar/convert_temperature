def convert_temperature(temp, unit):
    """
    Convert temperature between Fahrenheit and Celsius.

    Parameters:
    temp (float): The temperature value to convert.
    unit (str): The unit of the input temperature. 'F' for Fahrenheit, 'C' for Celsius.

    Returns:
    float: Converted temperature rounded to 2 decimal places.
    str: Error message if invalid unit is provided.
    """
    unit = unit.upper()
    
    if unit == 'F':
        # Fahrenheit to Celsius
        converted = (temp - 32) * 5 / 9
        return round(converted, 2)
    elif unit == 'C':
        # Celsius to Fahrenheit
        converted = (temp * 9 / 5) + 32
        return round(converted, 2)
    else:
        return "Error: Invalid unit! Please enter 'F' for Fahrenheit or 'C' for Celsius."

def main():
    print("Welcome to the Temperature Converter!")
    try:
        temp = float(input("Enter the temperature value to convert: "))
        unit = input("Enter the unit of the temperature ('F' for Fahrenheit, 'C' for Celsius): ").strip()
        
        result = convert_temperature(temp, unit)
        
        if isinstance(result, float):
            if unit.upper() == 'F':
                print(f"{temp}°F is {result}°C.")
            else:
                print(f"{temp}°C is {result}°F.")
        else:
            print(result)  # Print error message
    except ValueError:
        print("Error: Please enter a valid numerical temperature.")

if __name__ == "__main__":
    main()
