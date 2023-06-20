from collections import defaultdict


def main():
    N, Q = map(int, input().split())
    gragh = defaultdict(set)
    ans = N
    for q in range(Q):
        n, u, *v = list(map(int, input().split()))
        if n == 1:
            v = v[0]
            if not gragh[u]:
                ans -= 1
            if not gragh[v]:
                ans -= 1

            gragh[u].add(v)
            gragh[v].add(u)
        else:
            for vv in gragh[u]:
                gragh[vv].remove(u)
                if not gragh[vv]:
                    ans += 1

            ans += 1 if gragh[u] else 0
            gragh[u] = set()

        print(ans)


if __name__ == "__main__":
    main()
