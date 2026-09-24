numbers = [5, 5, 2, 8, 2, 5, 8, 8, 8]

freq = {}

for num in numbers:
    if num in freq:
        freq[num] = freq[num] + 1
    else:
        freq[num] = 1

print(freq)