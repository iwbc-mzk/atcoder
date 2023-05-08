from collections import defaultdict

def main():
    N, M = map(int, input().split())
    gragh = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)

    ans = 0
    for i in gragh:
        for j in gragh[i]:
            for k in gragh[j]:
                if k in gragh[i]:
                    ans += 1

    ans //= 6
    print(ans)


if __name__ == "__main__":
    main()