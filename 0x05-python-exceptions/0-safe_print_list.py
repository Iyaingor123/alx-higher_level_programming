#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x element of a list.

    Args:
    my_list (list): The list to print the element from
    x (int): the numer of elements of my_list to print

    Returns:
    The number of element printed.
    """
    num = 0
    for j in range(x):
        try:
            print("{}".format(my_list[j], end="")
            num += 1
        except IndexError:
            break
    print("")
    return (num)
