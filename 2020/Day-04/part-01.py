# Solution: 196

with open("input.txt", "r") as f:
    passports = list(map(lambda x : x.replace("\n", " ").strip(), f.read().split("\n\n")))

FIELDS = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]

valid = 0
for passport in passports:
    counter = 0
    for f in FIELDS:
        if f in passport:
            counter += 1
    
    valid += (1 if counter == 7 else 0)

print(valid)
