user_text = input()

user_text_lower_split = user_text.lower().split()
frequency = dict()

for word in set(user_text_lower_split):
    frequency[word] = user_text_lower_split.count(word)

sorted_frequency = sorted(frequency, key=frequency.get, reverse=True)

print(sorted_frequency[:5])
