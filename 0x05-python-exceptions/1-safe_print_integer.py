#!/usr/bin/python3
def safe_print_integer(value):
    try:
        formatted_value = "{:d}".format(value)  # Try to format the value as an integer
        print(formatted_value)  # Print the formatted value
        print()  # Print a new line
        return True
    except (ValueError, TypeError):
        return False
