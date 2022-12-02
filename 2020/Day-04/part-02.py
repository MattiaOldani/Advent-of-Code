# Solution: 114

with open("input.txt", "r") as f:
    passports = list(map(lambda x : x.replace("\n", " ").strip(), f.read().split("\n\n")))

FIELDS = [
    "byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"
]

RULES = {
    "byr" : lambda x : 1920 <= int(x) <= 2002,
    "iyr" : lambda x : 2010 <= int(x) <= 2020,
    "eyr" : lambda x : 2020 <= int(x) <= 2030,
    "hgt" : lambda x : 150 <= int(x[:len(x)-2]) <= 193 if x[-2:] == "cm" else 59 <= int(x[:len(x)-2]) <= 76,
    "hcl" : lambda x : x[0] == "#" and sum([1 for y in x[1:] if y in "0123456789abcdef"]) == 6,
    "ecl" : lambda x : x in "amb blu brn gry grn hzl oth",
    "pid" : lambda x : len(x) == 9 and sum([1 for y in x if y in "0123456789"]),
    "cid" : lambda x : True
}

valid = 0
for passport in passports:
    counter = 0
    for f in FIELDS:
        if f in passport:
            counter += 1
    
    if counter != 7:
        continue
    
    check = True
    new_fields = [x for x in FIELDS].append("cid")
    passport = passport.split(" ")
    for field in passport:
        field = field.split(":")
        check = check and RULES[field[0]](field[1])
    
    valid += (1 if check else 0)

print(valid)
