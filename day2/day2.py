# a, x  = rock
# b, y = paper
# c, z = scissors

shapes = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

outcomes = {
    "A": { "X": 3, "Y": 6, "Z": 0 },
    "B": { "X": 0, "Y": 3, "Z": 6 },
    "C": { "X": 6, "Y": 0, "Z": 3 }
}

def day2_pt1(input):
    total = 0
    for them, me in input:
        total += outcomes[them][me] + shapes[me]
    return total

results = {
    "X": 0,
    "Y": 3,
    "Z": 6
}

second_outcomes = {
    "A": { 3: "X", 6: "Y", 0: "Z" },
    "B": { 0: "X", 3: "Y", 6: "Z"},
    "C": { 6: "X", 0: "Y", 3: "Z" }
}

def day2_pt2(input):
    total = 0
    for them, me in input:
        my_throw = second_outcomes[them][results[me]]
        total += results[me] + shapes[my_throw]
    print(total)


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as f:
        f_data = [coord.split(' ') for coord in f.read().split('\n')]
        print(day2_pt1(f_data))
        print(day2_pt2(f_data))