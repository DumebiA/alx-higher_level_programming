#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0  # Initialize a counter to keep track of the number of elements printed
    try:
        for element in my_list:
            if count < x:
                print(element, end=" ")
                count += 1
        print()
        return count  # Return the actual number of elements printed
    except TypeError:
        print("Error: Input list must be iterable.")
        return count
