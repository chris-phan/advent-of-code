if __name__ == "__main__":
    f = open("input.txt", "r")
    cur = 50
    res = 0

    for line in f:
        l = line.strip()
        num = int(l[1:])

        if l[0] == "L":
            cur -= num
        else:
            cur += num
        cur = cur % 100
        
        if cur == 0:
            res += 1

    print(f"password: {res}")

