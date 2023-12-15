# Solution: 508552

with open("input.txt", "r") as f:
    words = f.read().strip().split(",")

count = 0
for word in words:
    current_value = 0
    for character in word:
        current_value = ((current_value + ord(character)) * 17) % 256 
    count += current_value

print(count)
