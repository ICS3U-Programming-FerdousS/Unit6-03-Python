#!/usr/bin/env python3
# Created By: Ferdous Sediqi
# Date: May 27, 2022
# This program we generate random number (0-100)
# then we store them in a list and display the min value of the array
# using a for each loop 

# import math random
import random

# function to find max value in the list
def find_min_value(list_of_number):
    
    # initialized
    min_value = 101
    # loop through the array to find max_num
    for number in list_of_number: 
        if  min_value > number:
            min_value = number
    return min_value

def main():
    # list size variable
    max_size = 10
    # empty list
    list_of_number = []
     # loop to generate random number and append it to list

    for counter in range(0, max_size, 1):
        # set random number between 0-100
        random_number = random.randint(0, 100)
        list_of_number.append(random_number)
        print(random_number, "added to the list in position", counter)
    # calling the function
    min_num = find_min_value(list_of_number)
    print("The min value is ", min_num)


if __name__ == "__main__":
    main()
