sentence = "apple banana apple orange banana apple"

words = sentence.split()

freq = {}

for word in words:
    if word in freq:
        freq[word] = freq[word] + 1
    else:
        freq[word] = 1

print(freq)