
"""def a_new_decorator(a_func):

    def wrapTheFunction():
        print("Before executing the function.")

        a_func()

        print("After executing function.")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("Decoration needed!")
"""

#edited with functools

from functools import wraps

def a_new_decorator(a_func):
    @wraps(a_func)
    def wrapTheFunction():
        print("Before executing the function.")

        a_func()

        print("After executing function.")
    return wrapTheFunction

@a_new_decorator
def a_function_requiring_decoration():
    print("Decoration needed!")


