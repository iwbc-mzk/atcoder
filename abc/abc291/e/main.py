import bisect
from collections import defaultdict
from queue import Queue


def main():
    N, M = map(int, input().split())
    XY = set(tuple(map(int, input().split())) for _ in range(M))

    gragh = {i: set() for i in range(1, N + 1)}
    into_num = [0 for _ in range(N)]
    for x, y in XY:
        gragh[x].add(y)
        into_num[y - 1] += 1

    q = Queue()
    for i in range(N):
        if into_num[i] == 0:
            q.put(i + 1)

    if q.qsize() != 1:
        print("No")
        return

    indexes = []
    while not q.empty():
        if q.qsize() != 1:
            print("No")
            return

        v = q.get()
        indexes.append(v)
        for vv in gragh[v]:
            into_num[vv - 1] -= 1
            if into_num[vv - 1] == 0:
                q.put(vv)

    ans = [-1 for _ in range(N)]
    for i, idx in enumerate(indexes, 1):
        ans[idx - 1] = i

    print("Yes")
    print(*ans)


if __name__ == "__main__":
    main()
