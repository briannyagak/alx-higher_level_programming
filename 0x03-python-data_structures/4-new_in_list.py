#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        modified_list = my_list[:idx] + [element] + my_list[idx + 1:]
    return modified_list
