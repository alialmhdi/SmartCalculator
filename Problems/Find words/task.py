user_input = input().split()
end_with_s = []
for word in user_input:
    if word.endswith("s"):
        end_with_s.append(word)
print("_".join(end_with_s))
