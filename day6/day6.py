
def day6(data, distinct_count):
    seen = []
    count = 0

    for c in data:
        if len(seen) == distinct_count:
            return count

        count += 1

        try:
            found = seen.index(c)
            seen = seen[found+1:]
            seen.append(c)
        except ValueError:
            seen.append(c)


if __name__ == "__main__":
    with open("./input.txt", "r", encoding="utf-8") as f:
        datastream =  f.read()
        print(day6(datastream, 4))
        print(day6(datastream, 14))
