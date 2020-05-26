# the list "girls" is already defined
cutest_girl = []
for girl in girls:
    if girl.get("education") == "MIT" and len(girl.get("about")) != 0:
        cutest_girl.append(girl.get("name"))
print(", ".join(cutest_girl))