def whitespace_split(input: str):
    res: list[str] = []
    cur = ""
    for c in input:
        if c == " ":
            if cur != "":
                res.append(cur)
            cur = ""
        else:
            cur += c
    if cur != "":
        res.append(cur)
    return res


if __name__ == "__main__":
    f = open("input.txt", "r")

    lines: list[list[str]] = []
    for line in f:
        lines.append(whitespace_split(line.strip()))

    res = 0
    for i in range(len(lines[0])):
        op = lines[-1][i]
        cur = int(lines[0][i])
        for j in range(1, len(lines) - 1):
            if op == "*":
                cur *= int(lines[j][i])
            else:
                cur += int(lines[j][i])
        res += cur

    print(f"res: {res}")

