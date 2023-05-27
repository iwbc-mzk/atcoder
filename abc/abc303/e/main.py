from collections import defaultdict
from queue import Queue


def main():
    N = int(input())

    gragh = defaultdict(list)
    for _ in range(N - 1):
        u, v = map(int, input().split())
        gragh[u].append(v)
        gragh[v].append(u)

    for k, v in gragh.items():
        if len(v) == 1:
            top = v[0]
            break

    q = Queue()
    q.put((top, 0))
    dist = [-1 for _ in range(N + 1)]
    visited = set()
    visited.add(top)
    while not q.empty():
        v, d = q.get()
        dist[v] = d
        for vv in gragh[v]:
            if vv not in visited:
                q.put((vv, d + 1))
                visited.add(vv)

    ans = []
    for i, d in enumerate(dist):
        if d % 3 == 0:
            ans.append(len(gragh[i]))

    ans.sort()
    print(*ans)


if __name__ == "__main__":
    main()
