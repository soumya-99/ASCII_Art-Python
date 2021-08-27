string = str(input("Enter a String: "))

char_frequency = {}

for char in string:
    if char in char_frequency:
        char_frequency[char] += 1
    else:
        char_frequency[char] = 1

print(
    f"Total length of the non-repeating substring is: {len(char_frequency.keys())}.")
