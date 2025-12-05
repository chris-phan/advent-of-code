if __name__ == "__main__":
    f = open("input.txt", "r")

    diagram: list[list[str]] = []
    for line in f:
        diagram.append([])
        for char in line:
            diagram[-1].append(char)

    def get_adj(r: int, c: int):
        dir = [-1, 0, 1]
        adj: list[str] = []
        for i in dir:
            for j in dir:
                if i == 0 and j == 0:
                    continue
                adj_r, adj_c = r + i, c + j
                if adj_r < 0 or adj_r >= len(diagram) or adj_c < 0 or adj_c >= len(diagram[0]):
                    continue
                adj.append(diagram[adj_r][adj_c])
        return adj

    res = 0
    for r in range(len(diagram)):
        for c in range(len(diagram[0])):
            if diagram[r][c] != "@":
                continue
            adj = get_adj(r, c)
            count = 0
            for char in adj:
                if char == "@":
                    count += 1
            if count < 4:
                res += 1

    print(f"res: {res}")
    

