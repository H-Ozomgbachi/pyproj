#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """prints x elements of a list

    Args:
        my_list (list, optional): Input List. Defaults to [].
        x (int, optional): num of el to print. Defaults to 0.

    Returns:
        int: real number of elements printed
    """
    num = 0
    try:
        for i in range(0,x):
            print(my_list[i], end="")
            num += 1
    except IndexError:
        pass
    print()
    return num
