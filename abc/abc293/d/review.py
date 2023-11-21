from collections import defaultdict, deque


def main():
    N, M = map(int, input().split())

    G = defaultdict(set)
    dg = [0 for _ in range(N + 1)]
    for _ in range(M):
        A, B, C, D = input().split()
        A = int(A)
        C = int(C)
        G[A].add(C)
        G[C].add(A)
        dg[A] += 1
        dg[C] += 1

    visited = set()
    l, nl = 0, 0
    for s in range(1, N + 1):
        if s in visited:
            continue

        q = deque()
        q.append(s)
        visited.add(s)
        loop = True
        while q:
            v = q.pop()
            loop &= dg[v] == 2
            for nv in G[v]:
                if nv not in visited:
                    q.append(nv)
                    visited.add(nv)

        if loop:
            l += 1
        else:
            nl += 1

    print(l, nl)


if __name__ == "__main__":
    main()
