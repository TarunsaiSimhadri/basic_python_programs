"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to 2^n table until n=entered value.

"""

N = int(input("enter n value:"))

if N<=0 and N>=31:
    print("N should be in between 0 and 31")
else:
    for i in range(N+1):
        print(2**i)
    