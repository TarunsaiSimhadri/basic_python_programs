"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to find Percentage of Head vs Tails when a coin is flipped for n times.

"""

import random

no_of_flips=int(input("enter no.of times should the coin flip:"))

heads=0
tails=0

for i in range(no_of_flips):
    if random.random()<0.5:
        tails+=1
    else:
        heads+=1
    
percentage_heads = heads/no_of_flips*100
percentage_tails = tails/no_of_flips*100

print(percentage_heads, "is percentage of heads")
print(percentage_tails, "is percentage of tails")