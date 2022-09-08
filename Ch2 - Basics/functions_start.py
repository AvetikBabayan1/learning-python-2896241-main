#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def func1():
    print("This is the 1st function")


# TODO: function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# TODO: function that returns a value
def func3(x):
    return (x ** 3)


# TODO: function with default value for an argument
def multip(number, level=3):
    result = 1
    for i in range(level):
        result = result * number
    return result


# TODO: function with variable number of arguments
def multi_arg(*args):
    result1= 0
    for i in args:
        result1=result1+i
    return result1

print(multi_arg(4,5,8,7,9,10))
