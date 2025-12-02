if __name__ == "__main__":
    f = open("input.txt", "r")
    cur = 50
    res = 0

    for line in f:
        l = line.strip()
        num = int(l[1:])

        if l[0] == "L":
            min_turns_for_zero = cur
            if cur == 0:
                min_turns_for_zero = 100
            if min_turns_for_zero <= num:
                # yes
                num -= min_turns_for_zero
                res += 1  # reached 0
                res += num // 100  # add remaining full rotations
                cur = (-1 * num) % 100
            else:
                # no
                cur -= num
        else:
            cur += num
            res += abs(cur // 100)

        cur = cur % 100

    print(f"password: {res}")

