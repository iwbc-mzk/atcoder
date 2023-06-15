from collections import defaultdict
from itertools import combinations
from queue import Queue


def main():
    N = int(input())
    sx, sy, tx, ty = map(int, input().split())
    XYR = [[i] + list(map(int, input().split())) for i in range(N)]

    XYR_comb = combinations(XYR, 2)
    gragh = defaultdict(set)
    start, end = -1, -1
    for (i1, x1, y1, r1), (i2, x2, y2, r2) in XYR_comb:
        dist = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if abs(r1 - r2) ** 2 <= dist <= (r1 + r2) ** 2:
            gragh[i1].add(i2)
            gragh[i2].add(i1)

        if start < 0:
            if (x1 - sx) ** 2 + (y1 - sy) ** 2 == r1**2:
                start = i1
            if (x2 - sx) ** 2 + (y2 - sy) ** 2 == r2**2:
                start = i2
        if end < 0:
            if (x1 - tx) ** 2 + (y1 - ty) ** 2 == r1**2:
                end = i1
            if (x2 - tx) ** 2 + (y2 - ty) ** 2 == r2**2:
                end = i2

    if start == end:
        print("Yes")
        return

    q = Queue()
    q.put(start)
    visited = set()
    visited.add(start)
    while not q.empty():
        v = q.get()
        for vv in gragh[v]:
            if vv == end:
                print("Yes")
                return
            if vv not in visited:
                q.put(vv)
                visited.add(vv)
    else:
        print("No")


if __name__ == "__main__":
    main()
