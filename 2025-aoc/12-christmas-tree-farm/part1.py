# ok

if __name__ == "__main__":
    f = open("input.txt", "r")

    lines: list[str] = []
    for line in f:
        lines.append(line.strip())

    res = 0
    for i in range(len(lines) - 1, -1, -1):
        if lines[i] == "":
            break
        input = lines[i].split(" ")
        x, y = input[0][:-1].split("x")
        tot_shape_area = 0
        for i in range(1, len(input)):
            tot_shape_area += int(input[i]) * 9
        if tot_shape_area <= int(x) * int(y):
            res += 1

    print(f"res: {res}")

