from collections import deque
from queue import LifoQueue


def main():
    N = int(input())

    gragh = {a :[] for a in range(1, N + 1)}
    for _ in range(N - 1):
        A, B = map(int, input().split())
        gragh[A].append(B)
        gragh[B].append(A)

    for key, l in gragh.items():
        gragh[key] = deque(sorted(l))

    first_from = [-1 for _ in range(N + 1)]
    q = LifoQueue()
    q.put(1)
    first_from[1] = 0
    visited = []
    while not q.empty():
        v = q.get()
        visited.append(v)

        while len(gragh[v]):
            vv = gragh[v].popleft()
            if first_from[vv] < 0:
                q.put(vv)
                first_from[vv] = v
                break
        else:
            if v != 1:
                q.put(first_from[v])

    print(*visited)


if __name__ == "__main__":
    main()
