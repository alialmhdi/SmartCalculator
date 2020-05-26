def sq_sum(*numbers):
    total = 0.0
    for number in numbers:
        total += float(number) * float(number)
    return total
