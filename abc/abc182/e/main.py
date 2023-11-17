import sys

sys.setrecursionlimit(10**9)


def main():
    H, W, N, M = map(int, input().split())
    L = set()
    for _ in range(N):
        A, B = map(int, input().split())
        L.add((A - 1, B - 1))
    B = set()
    for _ in range(M):
        C, D = map(int, input().split())
        B.add((C - 1, D - 1))

    HW = [[0 for _ in range(W)] for _ in range(H)]
    for h in range(H):
        flg = False
        for w in range(W):
            if (h, w) in L:
                flg = True
            if (h, w) in B:
                flg = False

            if flg:
                HW[h][w] = 1

        flg = False
        for w in range(W - 1, -1, -1):
            if (h, w) in L:
                flg = True
            if (h, w) in B:
                flg = False

            if flg:
                HW[h][w] = 1

    for w in range(W):
        flg = False
        for h in range(H):
            if (h, w) in L:
                flg = True
            if (h, w) in B:
                flg = False

            if flg:
                HW[h][w] = 1

        flg = False
        for h in range(H - 1, -1, -1):
            if (h, w) in L:
                flg = True
            if (h, w) in B:
                flg = False

            if flg:
                HW[h][w] = 1

    ans = sum(sum(h) for h in HW)
    print(ans)


if __name__ == "__main__":
    main()
