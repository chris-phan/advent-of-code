def leftmost_idx_of_max(arr: list[int]):
    maxi = -1
    idx = 0
    for i in range(len(arr)):
        if arr[i] > maxi:
            maxi = arr[i]
            idx = i
    return idx

if __name__ == "__main__":
    f = open("input.txt", "r")
    res = 0

    for line in f:
        line = line.strip()
        nums: list[int] = []
        for n in line:
            nums.append(int(n))

        joltage = 0
        left_bound = 0
        for i in range(12, 0, -1):
            maxi_idx = leftmost_idx_of_max(nums[left_bound:len(nums) - i + 1])
            # print(f"\tmaxi_idx: {maxi_idx}")
            joltage = joltage * 10 + nums[left_bound + maxi_idx]
            left_bound += maxi_idx + 1

        res += joltage

    print(f"res: {res}")



