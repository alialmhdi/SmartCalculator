from collections.abc import Hashable
# create your dictionary here
objects_dict = {}
for item in objects:
    if isinstance(item, Hashable):
        objects_dict[item] = hash(item)