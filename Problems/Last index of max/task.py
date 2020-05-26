def last_indexof_max(numbers_):
    # write the modified algorithm here
    index = 0
    for number in range(1, len(numbers_)):
        if numbers_[number] >= numbers_[index]:
            index = number
    return index
