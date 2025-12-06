if __name__ == "__main__":
    f = open("input.txt", "r")

    lines: list[str] = []
    for line in f:
        if line[-1] == "\n":
            line = line[:len(line) - 1]
        lines.append(line)

    new_problem_idx: list[int] = []
    for i in range(len(lines[0])):
        found_new_problem = True
        for j in range(len(lines)):
            if lines[j][i] != " ":
                found_new_problem = False
                break
        if found_new_problem:
            new_problem_idx.append(i)

    lines_split: list[list[str]] = []
    for i in range(len(lines)):
        lines_split.append([])
        cur_num = ""
        idx = 0
        for j in range(len(lines[0])):
            if j == new_problem_idx[idx]:
                idx += 1
                lines_split[-1].append(cur_num)
                cur_num = ""
                if idx == len(new_problem_idx):
                    lines_split[-1].append(lines[i][j + 1:])
                    break
                continue
            else:
                cur_num += lines[i][j]

    res = 0
    for c in range(len(lines_split[0])):
        op = lines_split[-1][c][0]
        nums: list[int] = []
        for i in range(len(lines_split[0][c])):
            cur_num = ""
            for r in range(len(lines_split) - 1):
                if lines_split[r][c][i] == " ":
                    continue
                cur_num += lines_split[r][c][i]
            nums.append(int(cur_num))
        if op == "*":
            val = 1
            for n in nums:
                val *= n
            res += val
        else:
            for n in nums:
                res += n

    print(f"res: {res}")

