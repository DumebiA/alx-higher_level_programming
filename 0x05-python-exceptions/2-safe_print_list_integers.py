#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0  # Initialize a counter for the number of integers printed
    i = 0  # Initialize an index for iterating through the list
    while count < x:
        try:
            value = my_list[i]
            formatted_value = "{:d}".format(value)
            print(formatted_value, end=" ")  # Print the formatted integer followed by a space
            count += 1
        except (ValueError, TypeError):
            pass  # Skip non-integer values
        except IndexError:
            break  # Break the loop if the end of the list is reached
        i += 1

    print()  # Print a new line
    return count
