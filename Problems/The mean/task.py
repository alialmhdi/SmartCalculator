list_of_numbers = input().strip()
sum_of_number = 0
for number in list_of_numbers:
    sum_of_number += int(number)
print(sum_of_number / len(list_of_numbers))
print("")