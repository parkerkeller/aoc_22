import string

characters = {char: i for i, char in enumerate(string.ascii_lowercase+string.ascii_uppercase, 1)}

def day3(inputs):
    total = 0
    for rucksack in inputs:
        mid = int(len(rucksack)/2)
        one = set(c for c in rucksack[0:mid])
        two = set(c for c in rucksack[mid:])
        total += characters[next(iter(one.intersection(two)))]
    return total


def splitter(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

def day3_part2(inputs):
    total = 0
    for one, two, three in splitter(inputs, 3):
        total += characters[next(iter(set(one).intersection(set(two)).intersection((set(three)))))]
    return total

if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as f:
        data = f.read().split('\n')
        print(day3(data))
        print(day3_part2(data))