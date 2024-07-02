"""

@Author: TarunSai
@Date: 2024-06-27
@Last Modified by: 
@Last Modified time: 
@Title : Program to check a number is prime or not.

"""
def is_Prime(number):

    """

    description:
        This function is used to check a number is prime or not.
    
    parameters:
        number(integer): The number which is going to check prime number or not.
        
    return:
        none

    """

    if number>1:
        for i in range(2,number//2+1):
            if number%i==0:
                print(number, "is not a prime number")
                break
        else:
            print(number, "is a prime number")
    else:
        print(number, "is not a prime number")
    
number=int(input("enter n value:"))

is_Prime(number)