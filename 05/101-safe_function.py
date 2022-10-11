#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        return fct(*args)
    except BaseException as ex:
        print(f"Exception: {ex}")
        return None
