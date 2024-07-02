"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to print the greatest number among three numbers.

"""

number1=int(input("enter a number:"))
number2=int(input("enter a number:"))
number3=int(input("enter a number:"))

if number1 >= number2 and number1 >= number3:
    print(number1)
elif number2 >= number1 and number2 >= number3:
    print(number2)
else:
    print(number3)