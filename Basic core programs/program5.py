"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to find the prime factors of the given number.

"""

n = int(input("enter n value:"))
factors=[]
divisor=2

while n>1:
    while n % divisor==0:
        factors.append(divisor)
        n//=divisor
    divisor+=1

print(factors)