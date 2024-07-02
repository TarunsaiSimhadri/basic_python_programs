"""

@Author: TarunSai
@Date: 2024-07-01
@Last Modified by: 
@Last Modified time: 
@Title : Program to find square root of a number.

"""


def sqrt(c):

    """

    description:
        finds a squarre root of the number
    
    parameters:
        c (integer) : number which we want the square root
    
    return:
        None

    """

    if c<0:
        print("number should be greater than 0")
    else:
        epsilon = 1e-15
        t =  c

        while abs(t-c / t) > epsilon * t:
            t = (c / t + t) / 2.0
        print(t)

def main():

    c = int(input("enter a number: "))
    sqrt(c)

if __name__ == "__main__":
    main()


