def dist(point1: list[int], point2: list[int]):
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2

if __name__ == "__main__":
    f = open("input.txt", "r")

    points: list[list[int]] = []
    for line in f:
        x, y, z = line.strip().split(",")
        points.append([int(x), int(y), int(z)])

    # [[distance, point1Idx, point2Idx]]
    distances: list[list[int]] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            distances.append([d, i, j])

    distances.sort()
    point_to_cluster: dict[int, int] = {}
    parent_cluster: dict[int, int] = {}
    cluster_num = 0
    connections = 0
    last_point1 = 0
    last_point2 = 0
    def get_parent_cluster(cluster: int):
        parent = cluster
        while parent_cluster.get(parent, -1) != -1:
            parent = parent_cluster.get(parent, -1)
        return parent

    for i in range(len(distances)):
        d, point1, point2 = distances[i]
        cluster1 = point_to_cluster.get(point1, -1)
        cluster2 = point_to_cluster.get(point2, -1)
        parent1 = get_parent_cluster(point_to_cluster.get(point1, -1))
        parent2 = get_parent_cluster(point_to_cluster.get(point2, -1))
        if parent1 == parent2:
            if parent1 == -1:
                # create new cluster
                point_to_cluster[point1] = cluster_num
                point_to_cluster[point2] = cluster_num
                cluster_num += 1
            else:
                # same cluster
                continue
        elif parent1 == -1 and parent2 != -1:
            # add to cluster
            point_to_cluster[point1] = parent2
        elif parent1 != -1 and parent2 == -1:
            # add to cluster
            point_to_cluster[point2] = parent1
        else:
            # merge clusters
            parent_cluster[parent1] = cluster_num
            parent_cluster[parent2] = cluster_num
            cluster_num += 1

        connections += 1
        if connections == len(points) - 1:
            last_point1 = point1
            last_point2 = point2
            break

    res = points[last_point1][0] * points[last_point2][0]
    print(f"res: {res}")

