"""

@Author: TarunSai
@Date: 2024-06-27
@Last Modified by:
@Last Modified time:
@Title : Program to print elapsed time.

"""


import time

def end_time():
    
    """

    description:
        This function is get the end time.
    
    parameters:
        none
        
    return:
        none    

    """

    input("press enter to stop the stop watch")
    print("time ended")
    global end_time
    end_time=time.time()
    print(end_time)


def start_time():
    
    """
    description:
        This function is get the starting time.
    
    parameters:
        none
        
    return:
        none    

    """

    input("press enter to start the stop watch")
    print("time started")
    global start_time
    start_time=time.time()
    print(start_time)
    end_time()

    
start_time()

elapsed_time = end_time - start_time
print(elapsed_time, "is elapsed time")


