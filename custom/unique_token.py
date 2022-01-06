import random as rd
import time  # to check the runing time takes the algorithm to run

def uniqid(length):
    """
    This is a unique number generator written by Adesanmi D. PraiseGod on 22/12/2021
    when writting code for PLEP project to asign unique id for CSC320 project clients
    """

    cap = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    sma = "abcdefghijklmnopqrstuvwxyz"
    num = "0123456789"
    sign = "~!@#$%^&*()_+-=/?<>`':;}{[]|,."

    key = [cap, sma, num]

    unique_no = ""

    start = time.time() #start time for the time check

    for i in range(length):
        choise = key[rd.randint(0, len(key)-1)]
        size = len(choise)
        unique_no += choise[rd.randint(0, size-1)]

    stop = time.time()  #the stop time for the the time check 

    #print(stop-start)  #printing the time spent to run the program
        
    return unique_no

    





# print(uniqid(16))

