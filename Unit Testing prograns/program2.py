"""

@Author: TarunSai
@Date: 2024-07-01
@Last Modified by: 
@Last Modified time: 
@Title : Program to convert temperature.

"""

def dayOfWeek(m, d, y):
    
    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31 * m0) // 12) % 7
    return d0

def main():

        m = int(input("enter month: "))
        d = int(input("enter day: "))
        y = int(input("enter year: "))
   
        day_of_week = dayOfWeek(m, d, y)
        print(day_of_week)

if __name__ == "__main__":
    main()
