from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    rev_G = defaultdict(set)
    for _ in range(M):
        A, B = map(int, input().split())
        G[A].add(B)
        rev_G[B].add(A)

    numbers = []
    visited = set()
    for i in range(1, N + 1):
        if i in visited:
            continue

        q = deque()
        q.append(i)

        while q:
            v = q.pop()

            if v < 0:
                numbers.append(-v)
                continue

            if v in visited:
                continue

            visited.add(v)

            q.append(-v)
            for vv in G[v]:
                if vv in visited:
                    continue
                q.append(vv)

    numbers.reverse()

    visited = set()
    U = []
    for i in numbers:
        if i in visited:
            continue

        if i == 2:
            pass

        q = deque()
        q.append(i)
        visited.add(i)
        u = set()
        while q:
            v = q.pop()
            u.add(v)

            for vv in rev_G[v]:
                if vv not in visited:
                    q.append(vv)
                    visited.add(vv)

        U.append(u)

    ans = 0
    for u in U:
        ans += len(u) * (len(u) - 1) // 2

    print(ans)


if __name__ == "__main__":
    main()
