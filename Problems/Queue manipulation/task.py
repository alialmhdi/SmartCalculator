from collections import deque

new_dque = deque()
for _i in range(int(input())):
    commands_list = input().split()
    if commands_list[0].isalpha():
        if commands_list[0] == "ENQUEUE":
            if commands_list[1].isdigit():
                new_dque.append(commands_list[1])
        elif commands_list[0] == "DEQUEUE":
            new_dque.popleft()
for number in new_dque:
    print(number)