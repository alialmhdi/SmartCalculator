def range_sum(numbers_, a_, b_):
    sum_of_number = 0
    list_of_numbers = is_list_numbers(numbers_)
    from_number = is_digit(a_)
    to_number = is_digit(b_)
    if list_of_numbers:
        for number in list_of_numbers:
            if from_number <= number <= to_number:
                sum_of_number += number
    return sum_of_number


def is_list_numbers(list_number):
    list_of_numbers = []
    if len(list_number) != 0:
        for number in list_number:
            if is_digit(number):
                list_of_numbers.append(int(number))
        return list_of_numbers
    else:
        return False


def is_digit(digit_numbers):
    if len(digit_numbers) > 1:
        return [int(number) for number in digit_numbers if number.isdigit()]
    if len(digit_numbers) == 1:
        return int(digit_numbers) if digit_numbers.isdigit() else False


numbers = "5 1 3 4 2"
a, b = "2 4".split()
if int(a) <= int(b):
    print(range_sum(numbers, a, b))
