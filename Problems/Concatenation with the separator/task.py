def concat(*args, sep=" "):
    words = []
    for word in args:
        words.append(word)
    return sep.join(words)