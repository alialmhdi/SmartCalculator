def tallest_people(**kwarg):
    sorted_list = []
    max_value = max(kwarg.values())
    for key in kwarg:
        if kwarg.get(key) == max_value:
            sorted_list.append(key)
    sorted_list.sort()
    for word in sorted_list:
        print(f"{word} : {kwarg.get(word)}")
