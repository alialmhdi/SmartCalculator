# put your python code here
def multiply(*args):
    result = 1
    for number in args:
        if number != 0:
            result *= number
    return result
