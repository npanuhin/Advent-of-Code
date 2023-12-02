from re import fullmatch


with open("input.txt") as file:
    target = tuple(map(int, fullmatch(
        r"target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)",
        file.readline().strip()
    ).groups()))
    target_x, target_y = target[:2], target[2:]

max_abs_y = max(map(abs, target_y))

print(max_abs_y * (max_abs_y - 1) // 2)
