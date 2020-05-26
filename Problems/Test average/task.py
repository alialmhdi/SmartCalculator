def average_mark(*args):
    total = 0
    for number in args:
        total += number
    return round(total / len(args), 1)