def myeval(string, i, j):
    result = None
    operation = None
    buff = ""

    while i < j:
        if string[i] in ('+', '*'):
            if result is None:
                result = int(buff)
            elif operation == '+':
                result += int(buff)
            else:
                result *= int(buff)

            operation = string[i]
            buff = ""

        elif string[i] == '(':
            k = i
            opened = 1
            while opened > 0:
                i += 1
                opened += 1 if string[i] == '(' else -1 if string[i] == ')' else 0

            buff = myeval(string, k + 1, i)

        else:
            buff += string[i]

        i += 1

    if buff:
        if result is None:
            result = int(buff)
        elif operation == '+':
            result += int(buff)
        else:
            result *= int(buff)

    return result


with open("input.txt", 'r', encoding="utf-8") as file:
    print(sum(
        myeval(line, 0, len(line)) for line in (line.strip().replace(' ', '') for line in file)
    ))
