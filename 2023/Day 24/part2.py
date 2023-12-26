import sympy as sp


with open('input.txt') as file:
    hailstones = [
        [list(map(int, item.split(','))) for item in line.split('@')]
        for line in filter(None, map(str.strip, file))
    ]

# We need to find the starting position and velocity of the rock, so that it can hit all hailstones:
# [(spx, spy, spz), (svx, svy, svz)]   # Naming: spx = Starting Position X, vz2 = Velocity Z for 2nd hailstone

# For each hailstone, we have time tN when the rock collides with it
# System of blocks of equations:

# spx + svx * t1 = px1 + vx1 * t1
# spy + svy * t1 = py1 + vy1 * t1
# spz + svz * t1 = pz1 + vz1 * t1

# spx + svx * t2 = px2 + vx2 * t2
# spy + svy * t2 = py2 + vy2 * t2
# spz + svz * t2 = pz2 + vz2 * t2

# spx + svx * t3 = px2 + vx2 * t3
# spy + svy * t3 = py2 + vy2 * t3
# spz + svz * t3 = pz2 + vz2 * t3

# ...

# Each block has 7 unknowns (spx, spy, spz, svx, svy, svz, tN),
# where (spx, spy, spz, svx, svy, svz) are repeated for each block

# Total number of unknowns for B blocks is 6 + B

# To solve the system of equations, it must have the same number of equations as unknowns:
# 3 * B = 6 + B  =>  B = 3
# So we can solve the system of equations using just 3 blocks


# First let's define all variables for the first 3 blocks:
(px1, py1, pz1), (vx1, vy1, vz1) = hailstones[0]
(px2, py2, pz2), (vx2, vy2, vz2) = hailstones[1]
(px3, py3, pz3), (vx3, vy3, vz3) = hailstones[2]

# Then we can define the unknowns and the equations:
spx, spy, spz, svx, svy, svz, t1, t2, t3 = unknowns = sp.symbols('spx, spy, spz, svx, svy, svz, t1, t2, t3')

equations = [
    sp.Eq(spx + svx * t1, px1 + vx1 * t1),
    sp.Eq(spy + svy * t1, py1 + vy1 * t1),
    sp.Eq(spz + svz * t1, pz1 + vz1 * t1),

    sp.Eq(spx + svx * t2, px2 + vx2 * t2),
    sp.Eq(spy + svy * t2, py2 + vy2 * t2),
    sp.Eq(spz + svz * t2, pz2 + vz2 * t2),

    sp.Eq(spx + svx * t3, px3 + vx3 * t3),
    sp.Eq(spy + svy * t3, py3 + vy3 * t3),
    sp.Eq(spz + svz * t3, pz3 + vz3 * t3)
]

spx, spy, spz, *_ = sp.solvers.solve(equations, unknowns)[0]

print(spx + spy + spz)
