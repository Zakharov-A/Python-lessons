from collections import Counter

phones = ["Iphone", "Samsuns", "LG", "Iphone", "HTC", "LG"]

count = Counter(phones)
print(count)
print(count["LG"])

text = "Hallo Hallo Hallo".lower().replace(" ", "")

text_count = Counter(text)
print(text_count)