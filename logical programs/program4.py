"""

@Author: TarunSai
@Date: 2024-06-27
@Last Modified by: 
@Last Modified time: 
@Title : Program to reverse a number.

"""


def reversing(number):

    """

    description:
        This function is used to reverse the given number.
    
    parameters:
        number(integer): The number which we want to reverse.
        
    return:
        none

    """

    dummy=number
    reversed=0
    while dummy>0:
        rem=dummy%10
        dummy//=10
        reversed=reversed*10+rem
    print(reversed)

number=int(input("enter a number:"))

reversing(number)



        


