from collections import defaultdict, deque


def main():
    N, X, Y = map(int, input().split())

    G = defaultdict(set)
    G[X].add(Y)
    G[Y].add(X)

    for i in range(1, N):
        G[i].add(i + 1)
        G[i + 1].add(i)

    dist = [0 for _ in range(N)]
    for i in range(1, N):
        q = deque()
        q.append((i, 0))

        dist[0] += 1

        visited = set()
        visited.add(i)

        while q:
            v, d = q.popleft()
            for vv in G[v]:
                if vv not in visited:
                    q.append((vv, d + 1))
                    if vv > i:
                        dist[d + 1] += 1
                    visited.add(vv)

    for i in range(1, N):
        print(dist[i])


if __name__ == "__main__":
    main()
