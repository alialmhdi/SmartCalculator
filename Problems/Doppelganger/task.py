from collections.abc import Hashable
from collections import Counter
# the object_list has already been defined
# write your code here
object_hash = {}
number = 0
for item in object_list:
    if isinstance(item, Hashable):
        times = Counter(object_list)[item]
        if times > 1:
            object_hash[item] = times
for n in object_hash:
    number += object_hash[n]
print(number)
