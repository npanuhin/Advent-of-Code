fields = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")  # All fields except "cid"

data = [{}]

with open("input.txt", 'r', encoding="utf-8") as file:
	for line in file:
	    if not line.strip():
	        data.append({})
	    else:
	        for passport in line.strip().split():
	            data[-1][passport.split(':')[0]] = passport.split(':')[1]

answer = 0

for passport in data:
    if all(field in passport for field in fields):
        answer += 1

print(answer)
