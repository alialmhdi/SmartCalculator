# put your python code here
from collections import deque


user_input = list(input())
right_break = []
left_break = []
bracket_deque = deque()
for bracket in user_input:
    if bracket == "(":
        bracket_deque.appendleft(bracket)
    elif bracket == ")":
        if len(bracket_deque) != 0:
            bracket_deque.pop()
        else:
            bracket_deque.append(bracket)

if len(bracket_deque) == 0:
    print("OK")
else:
    print("ERROR")
