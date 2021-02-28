class CombinedListItem:
    def __init__(self, value, link_prev=None, link_next=None):
        self.value = value
        self.prev = link_prev
        self.next = link_next


class CombinedList:
    def __init__(self, items):
        self.items = {}
        self.size = 0

        cur_item = None
        for value in items:
            cur_item = CombinedListItem(value, link_prev=cur_item)
            self.items[value] = cur_item
            self.size += 1
        self.last_item = cur_item

        for _ in range(self.size - 1):
            prev_item = cur_item.prev
            prev_item.next = cur_item
            cur_item = prev_item

        self.first_item = cur_item

        self.last_item.next = self.first_item
        self.first_item.prev = self.last_item

        self.min_item = self.items[min(self.items)]
        self.max_item = self.items[max(self.items)]

    def pop_item(self, cur_item):
        cur_item.prev.next = cur_item.next
        cur_item.next.prev = cur_item.prev
        self.size -= 1
        return cur_item

    def insert_after(self, target_item, item):
        item.prev = target_item
        item.next = target_item.next

        target_item.next.prev = item
        target_item.next = item

        self.size += 1

    def get_by_value(self, value):
        if value < self.min_item.value:
            return self.max_item
        return self.items[value]


with open("input.txt", 'r', encoding="utf-8") as file:
    cups = list(map(int, file.readline().strip()))

cups += list(range(max(cups) + 1, 1_000_001))

cur_cup = cups[0]

cups = CombinedList(cups)
cur_cup = cups.get_by_value(cur_cup)

min_cup, max_cup = cups.min_item, cups.max_item

for step in range(10_000_000):
    taken_cups = [cups.pop_item(cur_cup.next) for _ in range(3)]

    dest_cup = cur_cup
    while dest_cup == cur_cup or dest_cup in taken_cups:
        dest_cup = cups.get_by_value(dest_cup.value - 1)

    for taken_cup in reversed(taken_cups):
        cups.insert_after(dest_cup, taken_cup)

    cur_cup = cur_cup.next

cur_cup = cups.get_by_value(1)
print(cur_cup.next.value * cur_cup.next.next.value)
