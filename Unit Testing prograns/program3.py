"""

@Author: TarunSai
@Date: 2024-07-01
@Last Modified by: 
@Last Modified time: 
@Title : Program to convert temperature.

"""


def fahrenheit_to_celsius(fahrenheit):

    """

    description:
        Convert temperature from Fahrenheit to Celsius.
    
    Parameters:
        fahrenheit (float): Temperature in Fahrenheit
    
    Returns:
        float: Temperature converted to Celsius

    """

    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_fahrenheit(celsius):

    """

    description:
        Convert temperature from Celsius to Fahrenheit.
    
    Parameters:
        celsius (float): Temperature in Celsius
    
    Returns:
        float: Temperature converted to Fahrenheit

    """

    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def main():
    
    fahrenheit = float(input("enter fahrenheit: "))
    celsius = float(input("enter celcius: "))

    fahrenheitt = fahrenheit_to_celsius(fahrenheit)
    celsiuss = celsius_to_fahrenheit(celsius)

    print(fahrenheitt)
    print(celsiuss)

if __name__ == "__main__" :
    main()

