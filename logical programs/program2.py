"""

@Author: TarunSai
@Date: 2024-06-27
@Last Modified by: 
@Last Modified time: 
@Title : Program to checkk a given number is perfect or not.

"""


def is_Perfect(number):

    """

    description:
        This function is used to check a nuber is perfect or not.
    
    parameters:
        number(integer): The number which is going to check perfect number or not.
        
    return:
        none

    """

    divisor_sum=0
    for i in range(1,number//2+1):
        if number%i==0:
            divisor_sum+=i
    
    if divisor_sum==number:
        print(number, "is a perfect number")
    else:
        print(number, "is not a perfect number")

number=int(input("enter a number:"))

is_Perfect(number)
