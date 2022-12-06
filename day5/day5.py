#     [H]         [D]     [P]
# [W] [B]         [C] [Z] [D]
# [T] [J]     [T] [J] [D] [J]
# [H] [Z]     [H] [H] [W] [S]     [M]
# [P] [F] [R] [P] [Z] [F] [W]     [F]
# [J] [V] [T] [N] [F] [G] [Z] [S] [S]
# [C] [R] [P] [S] [V] [M] [V] [D] [Z]
# [F] [G] [H] [Z] [N] [P] [M] [N] [D]
#  1   2   3   4   5   6   7   8   9
from copy import deepcopy

containers = [
    ['F', 'C', 'J', 'P', 'H', 'T', 'W'],
    ['G', 'R', 'V', 'F', 'Z', 'J', 'B', 'H'],
    ['H', 'P', 'T', 'R', ],
    ['Z', 'S', 'N', 'P', 'H', 'T'],
    ['N', 'V', 'F', 'Z', 'H', 'J', 'C', 'D'],
    ['P', 'M', 'G', 'F', 'W', 'D', 'Z'],
    ['M', 'V', 'Z', 'W', 'S', 'J', 'D', 'P'],
    ['N', 'D', 'S'],
    ['D', 'Z', 'S', 'F', 'M']
]


def day5(data, reverse_me_please=False):
    new_container = deepcopy(containers)
    for row in data:
        items = row.split(' ')
        count, start, end = [int(items[i]) for i in (1, 3, 5)]

        popped = []
        for _ in range(0, count):
            popped.append(new_container[start-1].pop())

        if reverse_me_please:
            popped.reverse()

        new_container[end-1].extend(popped)

    results = [r[-1] for r in new_container]
    return ''.join(results)



if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as f:
        sections = f.read().split('\n')
        print(day5(sections))
        print(day5(sections, reverse_me_please=True))