# naive

if __name__ == "__main__":
    f = open("input.txt", "r")
    
    points: list[list[int]] = []
    for line in f:
        x, y = line.strip().split(",")
        points.append([int(x), int(y)])

    res = 0
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            area = (abs(points[i][0] - points[j][0]) + 1) * (abs(points[i][1] - points[j][1]) + 1)
            res = max(res, area)

    print(f"res: {res}")

