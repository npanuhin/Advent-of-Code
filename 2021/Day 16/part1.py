from math import prod


OPERATIONS = [
    sum, prod, min, max, None,
    lambda items: int(items[0] > items[1]),
    lambda items: int(items[0] < items[1]),
    lambda items: int(items[0] == items[1])
]


class Packet:
    def __init__(self):
        pass

    def read(self, string, pos=0):
        self.version = int(string[pos:(pos := pos + 3)], 2)
        self.type_id = int(string[pos:(pos := pos + 3)], 2)
        self.subpackets = []
        self.value = None

        if self.type_id == 4:
            value = []
            for i in range(pos, len(string), 5):
                value.append(string[i + 1:i + 5])
                if int(string[i]) == 0:
                    break
            pos = i + 5
            self.value = int(''.join(value), 2)

        # --- else: self.type_id != 4: ---

        elif int(string[pos:(pos := pos + 1)]) == 0:
            subpackets_end = int(string[pos:(pos := pos + 15)], 2) + pos
            while pos < subpackets_end:
                self.subpackets.append(subpacket := Packet())
                pos = subpacket.read(string, pos)

        else:
            subpackets_count = int(string[pos:(pos := pos + 11)], 2)
            for _ in range(subpackets_count):
                self.subpackets.append(subpacket := Packet())
                pos = subpacket.read(string, pos)

        return pos

    def version_sum(self):
        return self.version + sum(subpacket.version_sum() for subpacket in self.subpackets)


root_packet = Packet()

with open("input.txt") as file:
    packet = file.readline().strip()

    root_packet.read(bin(int(packet, 16))[2:].zfill(len(packet) * 4))

print(root_packet.version_sum())
