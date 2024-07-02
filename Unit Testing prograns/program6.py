"""

@Author: TarunSai
@Date: 2024-07-01
@Last Modified by: 
@Last Modified time: 
@Title : Program to convert temperature.

"""


def to_binary(n):
    
    """

    description:
        converts decimal to binary
    
    parameters:
        n (decimal) : number which we want to represent/convert into binary
    
    return:
        padded_binary_str

    """

    if n == 0:
        return '0' 
    
    binary_str = ''
    binary_str1 = ''

    
    while n > 0:

        bit = '1' if n % 2 == 1 else '0'
        binary_str = bit + binary_str
        n //= 2
    1 
    return binary_str

def main():
    
    try:
        decimal_number = int(input("Enter a decimal number: "))
        
        if decimal_number < 0:
            print("Decimal number must be non-negative.")
            return
        
        binary_representation = to_binary(decimal_number)
        
        print(f"Binary representation of {decimal_number}:")
        print(binary_representation)
    
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()