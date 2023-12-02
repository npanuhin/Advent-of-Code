class Image:
    def __init__(self, image: list[list[str]]):
        self.width, self.height = len(image[0]), len(image)
        self.image = image

    def expand(self, amount: int):
        self.width += amount * 2
        self.height += amount * 2
        self.image = sum((
            [['.'] * self.width] * amount,
            [['.'] * amount + row + ['.'] * amount for row in self.image],
            [['.'] * self.width] * amount
        ), [])

    def enhance(self, algorithm: list[str]):
        infinity_symbol = INFINITY_SYMBOL_DARK if self.image[0][0] == '.' else INFINITY_SYMBOL_LIGHT

        new_image = [[infinity_symbol] * self.width for _ in range(self.height)]

        for y in range(1, self.height - 1):
            for x in range(1, self.width - 1):
                pos = 0
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        pos <<= 1
                        pos += (self.image[y + dy][x + dx] == '#')

                new_image[y][x] = algorithm[pos]

        self.image = new_image


with open("input.txt") as file:
    algorithm = file.readline()

    INFINITY_SYMBOL_DARK = algorithm[0]
    INFINITY_SYMBOL_LIGHT = algorithm[2 ** 9 - 1]

    image = Image(list(map(list, filter(None, map(str.strip, file)))))


ENHANCEMENTS = 2

image.expand(ENHANCEMENTS + 1)

for _ in range(ENHANCEMENTS):
    image.enhance(algorithm)

print(sum(row.count('#') for row in image.image))
