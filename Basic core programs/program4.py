"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to find the nth harmonic value.

"""

N = int(input("enter n value:"))
nth_harmonic=1

if N<=0:
    print("N should be greater than 0")
else:
    for i in range(2,N+1):
        nth_harmonic+=1/i

    print(nth_harmonic)