from collections import deque

new_deque = deque()
number_of_op = int(input())
for _i in range(number_of_op):
    user_input = input().strip().split()
    if len(user_input) == 1:
        if user_input[0] == "POP":
            new_deque.pop()
    if len(user_input) > 1:
        action, number = user_input
        if action == "PUSH":
            new_deque.append(number)

if len(new_deque) != 0:
    for _n in range(len(new_deque)):
        print(new_deque.pop())
