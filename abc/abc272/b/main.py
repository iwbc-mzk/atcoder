from collections import defaultdict

def main():
    N, M = map(int, input().split())

    g = defaultdict(set)
    for _ in range(M):
        k, *x = map(int, input().split())
        for xi in x:
            for xii in x:
                g[xi].add(xii)

    ans = True
    for v in g.values():
        if len(v) != N:
            ans = False
            break

    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()