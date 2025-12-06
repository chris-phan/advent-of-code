if __name__ == "__main__":
    f = open("input.txt", "r")

    intervals: list[list[int]] = []
    for line in f:
        if line == "\n":
            break
        line = line.strip()
        l, r = line.split("-")
        intervals.append([int(l), int(r)])

    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    res = 0
    for i in range(len(merged)):
        res += merged[i][1] - merged[i][0] + 1
    
    print(f"res: {res}")





