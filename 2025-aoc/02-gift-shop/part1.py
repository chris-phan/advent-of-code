# naive

def has_seq_repeated_twice(id: int):
    if id <= 9:
        return False
    str_id = str(id)
    mid = len(str_id) // 2

    return str_id[:mid] == str_id[mid:]

if __name__ == "__main__":
    f = open("input.txt", "r")
    input = f.readline()
    input = input.split(",")

    res = 0
    for i in range(len(input)):
        bounds = input[i].strip().split("-")
        lo, hi = int(bounds[0]), int(bounds[1])

        for val in range(lo, hi + 1):
            if has_seq_repeated_twice(val):
                res += val

    print(f"res: {res}")

