from collections import deque
students_queue = deque()
for _i in range(int(input())):
    commands_input = input().strip().split()
    if commands_input[0] == "READY":
        students_queue.append(commands_input[1])
    if commands_input[0] == "PASSED":
        print(students_queue.popleft())
    if commands_input[0] == "EXTRA":
        students_queue.appendleft(students_queue[-1])
        students_queue.pop()
for name in students_queue:
    print(name)