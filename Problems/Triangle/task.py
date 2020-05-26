user_input = int(input().strip())
i = 0
count = 1
space = user_input
while i < user_input:
    number_of_space = " " * (space - 1)
    space_len = len(number_of_space)
    simple = ("#" * count)
    print((number_of_space + simple).center(user_input))
    i += 1
    count += 2
    space -= 1
