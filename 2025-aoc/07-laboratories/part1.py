if __name__ == "__main__":
    f = open("input.txt", "r")

    input: list[str] = []
    for line in f:
        input.append(line.strip())

    res = 0
    beams: list[bool] = []
    for i in range(len(input[0])):
        beams.append(input[0][i] == "S")

    for i in range(1, len(input)):
        new_beams = [False for _ in range(len(beams))]
        for j in range(len(beams)):
            if beams[j] == True and input[i][j] == "^":
                new_beams[j - 1] = True
                new_beams[j + 1] = True
                res += 1
            elif beams[j] == True and input[i][j] == ".":
                new_beams[j] = True
        beams = new_beams

    print(f"res: {res}")



