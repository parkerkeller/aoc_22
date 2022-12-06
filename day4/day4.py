def pair_formatter(data):
    formatted_pairs = []
    for range_pair in data:
        r1, r2 = range_pair.split(',')
        r1_lower, r1_upper = r1.split('-')
        r2_lower, r2_upper = r2.split('-')

        formatted_pairs.append((int(r1_lower), int(r1_upper), int(r2_lower), int(r2_upper)))
    return formatted_pairs


def day4(data):
    # In how many assignment pairs does one range fully contain the other?
    overlaps = 0

    for r1_lower, r1_upper, r2_lower, r2_upper in data:
        if (
            r1_lower >= r2_lower and r1_upper <= r2_upper
        ) or (
            r1_lower <= r2_lower and r1_upper >= r2_upper
        ):
            overlaps += 1

    return overlaps

def day4_pt2(data):
    # In how many assignment pairs do ranges overlap at _all_?
    overlaps = 0

    for ranges in data:
        r1_range = {*range(ranges[0], ranges[1]+1)}
        r2_range = {*range(ranges[2], ranges[3]+1)}

        if r1_range.intersection((r2_range)):
            overlaps += 1

    return overlaps


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as f:
        sections = pair_formatter(f.read().split('\n'))

        print(day4(sections))
        print(day4_pt2(sections))