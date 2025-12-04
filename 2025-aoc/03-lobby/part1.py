if __name__ == "__main__":
    f = open("input.txt", "r")
    res = 0

    for line in f:
        line = line.strip()
        nums: list[int] = []
        for n in line:
            nums.append(int(n))

        for i in range(9, -1, -1):
            try:
                tens_place_idx = nums.index(i)
            except ValueError:
                continue
            if tens_place_idx == len(nums) - 1:
                continue
            ones_place = max(nums[tens_place_idx + 1:])
            res += i * 10 + ones_place
            break

    print(f"res: {res}")


