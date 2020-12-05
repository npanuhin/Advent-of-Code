from re import fullmatch

fields = {  # All fields without "cid"
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,

    "hgt": lambda x:
        (x[-2:] == "cm" and 150 <= int(x[:-2]) <= 193) or
        (x[-2:] == "in" and 59 <= int(x[:-2]) <= 76),

    "hcl": lambda x: fullmatch(r"#[\da-f]{6}", x),

    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),

    "pid": lambda x: fullmatch(r"\d{9}", x)
}

with open("input.txt", 'r', encoding="utf-8") as file:
    inp = list(map(str.strip, file.readlines()))

data = [{}]

for line in inp:
    if not line:
        data.append({})
    else:
        for passport in line.split():
            data[-1][passport.split(':')[0]] = passport.split(':')[1]

answer = 0

for passport in data:

    if not all(field in passport for field in fields):
        continue

    for field, checker in fields.items():
        try:
            if not checker(passport[field]):
                break
        except ValueError:
            break

    else:
        answer += 1

print(answer)
