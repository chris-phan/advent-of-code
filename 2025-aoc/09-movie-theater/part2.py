# sucks

class Point:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

if __name__ == "__main__":
    f = open("fail.txt", "r")
    
    points: list[Point] = []
    for line in f:
        x, y = line.strip().split(",")
        points.append(Point(int(x), int(y)))

    areas: list[list[int]] = []
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            area = (abs(points[i].x - points[j].x) + 1) * (abs(points[i].y - points[j].y) + 1)
            areas.append([area, i, j])

    """
    idea is to find a pair of points that form a rectangle
    that doesn't intersect with any of the edges of the overall shape
      - so, check each pair of points:
        for each pair, check that all the edges are either
          - to the left
          - to the right
          - above
          - below
        the rectangle

    sort by area so that the first pair found has the greatest area

    doesn't work in the general case since this doesn't account for the
    case where a rectangle is outside of the overall shape
    e.g.:      ##
               XX
               XX
               XX
               XX
               XX
               XX
               X#XXXXX#
               #XXXXXX#
          #: red tile
          X: green tile
          input: 0,0 0,8 7,8 7,7 1,7 1,0
    algorithm will say that the biggest is (56):
               #OOOOOOO
               XOOOOOOO
               XOOOOOOO
               XOOOOOOO
               XOOOOOOO
               XOOOOOOO
               XOOOOOOO
               XOOOOOOO
               #XXXXXX#
    when it's actually (18)
               OO
               OO
               OO
               OO
               OO
               OO
               OO
               OOXXXXX#
               OOXXXXX#
    """

    areas.sort(reverse=True)

    edges: list[list[Point]] = []
    for i in range(len(points) - 1):
        edges.append([points[i], points[i + 1]])
    edges.append([points[-1], points[0]])

    res = 0
    for i in range(len(areas)):
        area, p1Idx, p2Idx = areas[i]
        p1, p2 = points[p1Idx], points[p2Idx]
        done = True
        for j in range(len(edges)):
            e1, e2 = edges[j]
            edge_is_left = max(e1.x, e2.x) <= min(p1.x, p2.x)
            edge_is_right = min(e1.x, e2.x) >= max(p1.x, p2.x)
            edge_is_above = max(e1.y, e2.y) <= min(p1.y, p2.y)
            edge_is_below = min(e1.y, e2.y) >= max(p1.y, p2.y)
            edge_intersect = not edge_is_left and not edge_is_right and not edge_is_above and not edge_is_below
            if edge_intersect:
                done = False
                break

        if done:
            res = area
            print(p1.x, p1.y, p2.x, p2.y)
            break

    print(f"res: {res}")


