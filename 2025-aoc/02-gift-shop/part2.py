# naive

def has_repeating_seq(id: int):
    if id <= 9:
        return False

    str_id = str(id)
    for i in range(1, len(str_id) // 2 + 1):
        is_repeating = True
        if len(str_id) % i != 0:
            continue
        for j in range(i, len(str_id) - i + 1, i):
            if str_id[:i] != str_id[j:j+i]:
                is_repeating = False
                break
        if is_repeating:
            return True

    return False

if __name__ == "__main__":
    f = open("input.txt", "r")
    input = f.readline()
    input = input.split(",")

    res = 0
    for i in range(len(input)):
        bounds = input[i].strip().split("-")
        lo, hi = int(bounds[0]), int(bounds[1])

        for val in range(lo, hi + 1):
            if has_repeating_seq(val):
                res += val

    print(f"res: {res}")


