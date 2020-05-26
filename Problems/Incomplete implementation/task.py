def startswith_capital_counter(words):
    counter = 0
    for name in words:
        if name[0].isupper():
            counter += 1
    return counter
