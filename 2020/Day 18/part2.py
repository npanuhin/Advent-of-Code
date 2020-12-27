def myeval_plus(string, i, j):
    result = 0
    buff = ""

    while i < j:
        if string[i] == '+':
            result += int(buff)
            buff = ""

        elif string[i] == '(':
            k = i
            opened = 1
            while opened > 0:
                i += 1
                opened += 1 if string[i] == '(' else -1 if string[i] == ')' else 0

            buff = myeval_multiply(string, k + 1, i)

        else:
            buff += string[i]

        i += 1

    if buff:
        result += int(buff)

    return result


def myeval_multiply(string, i, j):
    result = 1
    k = i

    while i < j:
        if string[i] == '*':
            result *= myeval_multiply(string, k, i)
            k = i + 1

        elif string[i] == '(':
            opened = 1
            while opened > 0:
                i += 1
                opened += 1 if string[i] == '(' else -1 if string[i] == ')' else 0

        i += 1

    if k != i:
        result *= myeval_plus(string, k, i)

    return result


with open("input.txt", 'r', encoding="utf-8") as file:
    print(sum(
        myeval_multiply(line, 0, len(line)) for line in (line.strip().replace(' ', '') for line in file)
    ))
