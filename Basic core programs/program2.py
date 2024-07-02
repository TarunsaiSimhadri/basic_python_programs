"""

@Author: TarunSai
@Date: 2024-06-26
@Last Modified by: Tarunsai
@Last Modified time: 2024-06-27
@Title : Program to find the year is leap year or not.

"""

year=int(input("enter a year:"))

if year % 400==0 and year % 100==0:
    print(year, "is a leap year")
elif year % 4==0 and year % 100!=0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
    
    