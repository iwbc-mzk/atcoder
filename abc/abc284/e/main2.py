from collections import defaultdict, deque

MAX = 10**6


def main():
    N, M = map(int, input().split())

    gragh = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)

    ans = 0
    q = deque()
    q.append(~1)
    q.append(1)

    visited = set()
    visited.add(1)

    while len(q):
        v = q.pop()
        if v >= 0:
            ans += 1
            if ans >= MAX:
                break

            visited.add(v)

            for vv in gragh[v]:
                if vv not in visited:
                    q.append(~vv)
                    q.append(vv)
        else:
            visited.remove(~v)

    print(min(ans, MAX))


if __name__ == "__main__":
    main()
