if __name__ == "__main__":
    f = open("input.txt", "r")

    adj_list: dict[str, list[str]] = {}
    reverse_adj_list: dict[str, list[str]] = {}
    counts: dict[str, int] = {}
    for line in f:
        items = line.strip().split(" ")
        key = items[0][:-1]
        adj_list[key] = []
        counts[key] = -1
        for i in range(1, len(items)):
            adj_list[key].append(items[i])

            if items[i] not in reverse_adj_list:
                reverse_adj_list[items[i]] = []
            reverse_adj_list[items[i]].append(key)

    adj_list["out"] = []
    counts["out"] = -1
    def get_num_paths(cur: str, dest: str):
        for k in counts.keys():
            counts[k] = -1

        def num_paths(cur: str, dest: str):
            if cur == dest:
                return 1

            tot: int = 0
            for i in range(len(adj_list[cur])):
                c = counts[adj_list[cur][i]]
                if c == -1:
                    c = num_paths(adj_list[cur][i], dest)
                    counts[adj_list[cur][i]] = c
                tot += c

            return tot
        
        return num_paths(cur, dest)

    # Since this is a DAG, either dac comes first in the path from
    # svr -> out or fft comes first
    # It's not possible to have both a path svr...dac...fft...out
    # and svr...fft...dac...out since there'd be a cycle
    res = 0
    dac_fft = get_num_paths("dac", "fft")
    if dac_fft != 0:
        # dac comes first
        seg1 = get_num_paths("svr", "dac")
        seg2 = dac_fft
        seg3 = get_num_paths("fft", "out")
        res = seg1 * seg2 * seg3
    else:
        # fft comes first
        seg1 = get_num_paths("svr", "fft")
        seg2 = get_num_paths("fft", "dac")
        seg3 = get_num_paths("dac", "out")
        res = seg1 * seg2 * seg3

    print(f"res: {res}")

