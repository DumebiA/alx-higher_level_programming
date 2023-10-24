#!/usr/bin/python3
def safe_print_division(a, b):
    result = None  # Initialize the result to None
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("Inside result: {}".format(result))
    return result
