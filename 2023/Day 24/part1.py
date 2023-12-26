POS_MIN = 200_000_000_000_000
POS_MAX = 400_000_000_000_000

# POS_MIN = 7
# POS_MAX = 27

with open('input.txt') as file:
    hailstones = [
        [list(map(int, item.split(','))) for item in line.split('@')]
        for line in filter(None, map(str.strip, file))
    ]

intersections = 0

for i in range(len(hailstones)):
    for j in range(i + 1, len(hailstones)):
        (px1, py1, _), (vx1, vy1, _) = hailstones[i]
        (px2, py2, _), (vx2, vy2, _) = hailstones[j]

        # System of equations (t1 and t2 is time):
        #   px1 + vx1 * t1 = px2 + vx2 * t2
        #   py1 + vy1 * t1 = py2 + vy2 * t2

        # Solving for t1 and t2:
        #   t1 = (px2 + vx2 * t2 - px1) / vx1
        #   t2 = (py1 + vy1 * t1 - py2) / vy2
        #      = (py1 + vy1 * (px2 + vx2 * t2 - px1) / vx1 - py2) / vy2
        #      = (py1 / vy2) + ((vy1 * px2 + vy1 * vx2 * t2 - vy1 * px1) / vx1 / vy2) - (py2 / vy2)
        #      = (py1 / vy2) + ((vy1 * px2 - vy1 * px1) / vx1 / vy2) + ((vy1 * vx2 * t2) / vx1 / vy2) - (py2 / vy2)
        #      = (py1 / vy2) + ((vy1 * px2 - vy1 * px1) / vx1 / vy2) + t2 * ((vy1 * vx2) / vx1 / vy2) - (py2 / vy2)

        #   t2 * (1 - ((vy1 * vx2) / vx1 / vy2)) = (py1 / vy2) + ((vy1 * px2 - vy1 * px1) / vx1 / vy2) - (py2 / vy2)
        #   t2 * (1 - ((vy1 * vx2) / vx1 / vy2)) = (py1 + ((vy1 * px2 - vy1 * px1) / vx1) - py2) / vy2
        #   t2 * (vy2 - ((vy1 * vx2) / vx1)) = (py1 + ((vy1 * px2 - vy1 * px1) / vx1) - py2)
        #   t2 = (py1 + ((vy1 * px2 - vy1 * px1) / vx1) - py2) / (vy2 - ((vy1 * vx2) / vx1))

        if (vy2 - ((vy1 * vx2) / vx1)) == 0:
            continue

        t2 = (py1 + ((vy1 * px2 - vy1 * px1) / vx1) - py2) / (vy2 - ((vy1 * vx2) / vx1))
        t1 = (px2 + vx2 * t2 - px1) / vx1

        if t1 < 0 or t2 < 0:
            continue

        x1 = px1 + vx1 * t1
        y1 = py1 + vy1 * t1

        # x2 and y2 can be used to check correctness
        # x2 = px2 + vx2 * t2
        # y2 = py2 + vy2 * t2

        if POS_MIN <= x1 <= POS_MAX and POS_MIN <= y1 <= POS_MAX:
            intersections += 1

print(intersections)
