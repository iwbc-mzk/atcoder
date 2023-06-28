from collections import defaultdict
import sys

sys.setrecursionlimit(10**7)


def main():
    N, M = map(int, input().split())

    gragh = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)

    ans = 0

    def rec(v: int, visited: set):
        nonlocal ans
        ans += 1
        if ans > 10**6:
            return
        for vv in gragh[v]:
            if vv not in visited:
                visited.add(vv)
                rec(vv, visited)
                visited.remove(vv)

    rec(1, set([1]))
    print(min(ans, 10**6))


if __name__ == "__main__":
    main()
