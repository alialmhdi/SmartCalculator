n = int(input())
my_stack = []
for _i in range(n):
    my_stack.append(input())
for _latter in range(n):
    print(my_stack.pop())
