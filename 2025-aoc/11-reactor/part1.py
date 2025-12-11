if __name__ == "__main__":
    f = open("input.txt", "r")

    adj_list: dict[str, list[str]] = {}
    for line in f:
        items = line.strip().split(" ")
        key = items[0][:-1]
        adj_list[key] = []
        for i in range(1, len(items)):
            adj_list[key].append(items[i])

    def num_paths(cur: str):
        if cur == "out":
            return 1

        tot: int = 0
        for i in range(len(adj_list[cur])):
            tot += num_paths(adj_list[cur][i])

        return tot
    
    res = num_paths("you")
    print(f"res: {res}")

