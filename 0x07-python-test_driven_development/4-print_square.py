#!/usr/bin/python3
def print_square(size):
    # Check if size is an integer
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check if size is greater than or equal to 0
    if size < 0:
        raise ValueError("size must be >= 0")

    # Check if size is a float and is less than 0
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    # Print the square
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print("")

if __name__ == "__main__":
    print_square(4)
    print("")
    print_square(10)
    print("")
    print_square(0)
    print("")
    print_square(1)
    print("")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
