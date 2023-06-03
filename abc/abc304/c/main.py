from itertools import combinations
from collections import defaultdict
import math
from queue import Queue


def main():
    N, D = map(int, input().split())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    comb = combinations(XY, 2)
    gragh = defaultdict(set)
    for (x1, y1), (x2, y2) in comb:
        dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if dist <= D:
            gragh[(x1, y1)].add((x2, y2))
            gragh[(x2, y2)].add((x1, y1))

    ans = {xy: False for xy in XY}
    start = XY[0]
    ans[start] = True
    q = Queue()
    q.put(start)
    visited = set()
    visited.add(start)
    while not q.empty():
        v = q.get()
        for vv in gragh[v]:
            if vv not in visited:
                q.put(vv)
                ans[vv] = True
                visited.add(vv)

    for xy in XY:
        print("Yes" if ans[xy] else "No")


if __name__ == "__main__":
    main()
