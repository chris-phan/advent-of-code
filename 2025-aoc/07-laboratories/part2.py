if __name__ == "__main__":
    f = open("input.txt", "r")

    input: list[str] = []
    for line in f:
        input.append(line.strip())

    res = 0
    tmp = []
    num_beams: list[int] = []
    for i in range(len(input[0])):
        if input[0][i] == "S":
            num_beams.append(1)
        else:
            num_beams.append(0)

    for i in range(1, len(input)):
        new_num_beams: list[int] = [0] * len(num_beams)
        for j in range(len(num_beams)):
            if num_beams[j] > 0 and input[i][j] == "^":
                new_num_beams[j - 1] += num_beams[j]
                new_num_beams[j + 1] += num_beams[j]
            elif num_beams[j] > 0 and input[i][j] == ".":
                new_num_beams[j] += num_beams[j]
        num_beams = new_num_beams

    print(f"res: {sum(num_beams)}")

