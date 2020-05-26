# put your python code here
first_number = float(input())
second_number = float(input())
operation = input()
result = ""

if operation == "mod":
    if second_number != 0:
        result = first_number % second_number
    else:
        result = "Division by 0!"

elif operation == "div":
    if second_number != 0:
        result = first_number // second_number
    else:
        result = "Division by 0!"
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Division by 0!"
elif operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "pow":
    result = first_number ** second_number
print(result)
