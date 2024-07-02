"""

@Author: TarunSai
@Date: 2024-06-27
@Last Modified by: 
@Last Modified time: 
@Title : Program to print fibonacci series.

"""


def fibonacci(n):

    """

    description:
        This function is used to print the fibonacci series
    
    parameters:
        n(integer): To print n no.of fibonacci series
        
    return:
        none

    """
    
    number1=int(input("enter a value:"))
    number2=int(input("enter b value:"))

    if n<=0:
        print("n should be greater than 0")
    elif n==1:
        print(number1)
    elif n==2:
        print(number1, number2)
    else:
        print(number1, number2, end=' ')
        for i in range(n-2):
            number3 = number1+number2
            number1, number2=number2, number3
            print(number3, end=' ')

n=int(input("enter n value:"))   

fibonacci(n)
