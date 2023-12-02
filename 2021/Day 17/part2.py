from re import fullmatch


def sign(x):
    return 1 if x > 0 else -1 if x < 0 else 0


with open("input.txt") as file:
    target = tuple(map(int, fullmatch(
        r"target area: x=([\d-]+)..([\d-]+), y=([\d-]+)..([\d-]+)",
        file.readline().strip()
    ).groups()))
    target_x, target_y = target[:2], target[2:]

# max_abs_x = max(map(abs, target_x))
max_abs_y = max(map(abs, target_y))

min_x = min(0, min(target_x))
max_x = max(0, max(target_x))
min_y = min(0, min(target_y))
max_y = max_abs_y * (max_abs_y - 1) // 2


def test(vx, vy):
    x = y = 0
    while min_x <= x <= max_x and min_y <= y <= max_y:
        x += vx
        y += vy
        vx -= sign(vx)
        vy -= 1

        if target_x[0] <= x <= target_x[1] and target_y[0] <= y <= target_y[1]:
            return True
    return False


print(sum(
    test(vx, vy)
    for vx in range(min_x, max_x + 1)
    for vy in range(min_y, max_abs_y + 1)
))
