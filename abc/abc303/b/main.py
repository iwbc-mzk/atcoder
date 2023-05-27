from collections import defaultdict

def main():
    N, M = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(M)]

    g = defaultdict(set)
    for a in A:
        for i in range(N - 1):
            g[a[i]].add(a[i + 1])
            g[a[i + 1]].add(a[i])
    ans = 0
    for gi in g.values():
        ans += N - len(gi) - 1

    ans //= 2
    print(ans)



if __name__ == "__main__":
    main()
