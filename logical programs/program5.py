"""
@Author: TarunSai
@Date: 2024-06-27
@Last Modified by: 
@Last Modified time: 
@Title : Program to print random copouns without duplicates and print them.

"""

import random

def distinct_copoun_number(N):
    """
    description:
        This function is used to get the random copoun numbers without repeating/duplicates.
    
    parameters:
        N(integer): no.of random copouns need to be printed. 
        
    return:
        none    

    """

    collected_copoun_numbers=set()
    total_collected_copoun_numbers=0

    while len(collected_copoun_numbers)<N:
        copoun_number=random.randint(1,100)
        collected_copoun_numbers.add(copoun_number)
        print(copoun_number)
        total_collected_copoun_numbers+=1

    print(total_collected_copoun_numbers)
    

N=int(input("enter N value:"))

distinct_copoun_number(N)

