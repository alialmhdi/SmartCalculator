text = input()
text2 = text.lower()
words = text2.split()
text3 = text.split()
website_index = []
website = []
count = 0
for word in words:
    if word.startswith("https://") or word.startswith("http://") or word.startswith("www."):
        website_index.append(count)
    count += 1
for index in website_index:
    website.append(text3[index])
if len(website) != 0:
    print("\n".join(website))
