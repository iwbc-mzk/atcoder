from collections import defaultdict


def main():
    N, M = map(int, input().split())

    G = defaultdict(int)
    for _ in range(M):
        a, b = map(int, input().split())
        if b < a:
            G[a] += 1
        elif a < b:
            G[b] += 1
        else:
            ...

    ans = 0
    for v in G.values():
        if v == 1:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
