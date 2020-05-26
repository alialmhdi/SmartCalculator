from collections import deque

order_list = deque()
for _n in range(int(input())):
    orders = input().strip().split()
    if orders[0] == "ISSUE":
        order_list.append(orders[1])
    if orders[0] == "SOLVED":
        order_list.popleft()
for order in order_list:
    print(order)