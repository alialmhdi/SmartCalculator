# the list "walks" is already defined
# your code here
total = 0
for value in walks:
    total += value.get("distance")
print(total // len(walks))