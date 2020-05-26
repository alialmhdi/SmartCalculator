# put your python code here
from collections import Counter

user_input = input().split()
user_dict = [item.lower() for item in user_input]
for litter, count in Counter(user_dict).items():
    print(litter, count)
