# put your python code here
user_input = input().split()
magic_number = input()
list_of_num = []
position = 0
if magic_number in user_input:
    for number in user_input:
        if magic_number == number:
            list_of_num.append(str(position))
        position += 1
    print(" ".join(list_of_num))
else:
    print("not found")
