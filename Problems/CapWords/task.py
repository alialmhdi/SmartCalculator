user_input = input()
user_input_list = user_input.split("_")
words = []
if len(user_input_list) >= 2:
    for word in user_input_list:
        words.append(word.capitalize())
    print("".join(words))
else:
    print(user_input.capitalize())