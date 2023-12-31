#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            value_1 = my_list_1[i] if i < len(my_list_1) else 0
            value_2 = my_list_2[i] if i < len(my_list_2) else 0

            if not isinstance(value_1, (int, float)) or not isinstance(value_2, (int, float)):
                result.append("wrong type")
            elif value_2 == 0:
                result.append("division by 0")
            else:
                result.append(value_1 / value_2)
        except IndexError:
            print("out of range")
            break
        finally:
            if i == list_length - 1:
                return resulti
