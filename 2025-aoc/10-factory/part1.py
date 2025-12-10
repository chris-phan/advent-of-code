def copy_subset(subset: list[list[int]]):
    res: list[list[int]] = []
    for s in subset:
        res.append(s.copy())
    return res

def power_set(input_set: list[list[int]]):
    res: list[list[list[int]]] = []
    def dfs(idx: int, cur_subset: list[list[int]]):
        if idx >= len(input_set):
            res.append(copy_subset(cur_subset))
            return

        # include
        cur_subset.append(input_set[idx])
        dfs(idx + 1, cur_subset)

        _ = cur_subset.pop()

        # don't include
        dfs(idx + 1, cur_subset)

    dfs(0, [])
    return res


if __name__ == "__main__":
    f = open("input.txt", "r")

    indicator_lights: list[list[int]] = []
    buttons: list[list[list[int]]] = []

    for line in f:
        line_items = line.strip().split(" ")

        indicator_lights.append([])
        for c in line_items[0][1:-1]:
            if c == "#":
                indicator_lights[-1].append(True)
            else:
                indicator_lights[-1].append(False)

        buttons.append([])
        for button in line_items[1:-1]:
            button_nums = button[1:-1].split(",")
            int_buttons: list[int] = []
            for i in range(len(button_nums)):
                int_buttons.append(int(button_nums[i]))
            buttons[-1].append(int_buttons)

    res = 0
    for i in range(len(buttons)):
        all_subsets = power_set(buttons[i])
        all_subsets.sort(key=lambda x: len(x))

        for subset in all_subsets:
            freq = [0] * len(indicator_lights[i])
            for j in range(len(subset)):
                for k in range(len(subset[j])):
                    freq[subset[j][k]] += 1
            found = True
            for j in range(len(indicator_lights[i])):
                if ((indicator_lights[i][j] and freq[j] % 2 == 0) or
                    (not indicator_lights[i][j] and freq[j] % 2 != 0)):
                    found = False
                    break

            if found:
                res += len(subset)
                break

    print(f"res: {res}")

