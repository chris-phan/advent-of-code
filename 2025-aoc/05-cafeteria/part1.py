if __name__ == "__main__":
    f = open("input.txt", "r")

    intervals: list[list[int]] = []
    ids: list[int] = []
    done_reading_intervals = False
    for line in f:
        if line == "\n":
            done_reading_intervals = True
            continue
        line = line.strip()
        if not done_reading_intervals:
            l, r = line.split("-")
            intervals.append([int(l), int(r)])
        else:
            ids.append(int(line))

    intervals.sort()
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        if merged[-1][1] >= intervals[i][0]:
            merged[-1][1] = max(merged[-1][1], intervals[i][1])
        else:
            merged.append(intervals[i])

    res = 0
    for id in ids:
        for i in range(len(merged)):
            if merged[i][0] <= id <= merged[i][1]:
                res += 1
    
    print(f"res: {res}")




