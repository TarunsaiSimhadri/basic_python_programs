"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to print an alphabet is vowel or consonant.

"""

n=input("enter an alphabet:")
vowels='aeiouAEIOU'

if n in vowels:
    print(n, "is a vowel")
else:
    print(n, "is a consonant")