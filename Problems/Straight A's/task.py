# put your python code here
user_input = input()
number_of_a = user_input.count("A")
total = len(user_input.split())
result = number_of_a / total
print(round(float(result), 2))
