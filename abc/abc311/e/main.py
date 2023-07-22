import bisect


def main():
    H, W, N = map(int, input().split())

    HW = [[1 for _ in range(W)] for _ in range(H)]
    for _ in range(N):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        HW[a][b] = -1

    for i in range(H):
        flg = True
        for j in range(1, W):
            if HW[i][j] == -1:
                flg = False

            if flg:
                HW[i][j] += HW[i][j - 1]
            else:
                HW[i][j] = -1

    for j in range(W):
        flg = True
        for i in range(1, H):
            if HW[i][j] == -1:
                flg = False

            if flg:
                HW[i][j] += HW[i - 1][j]
            else:
                HW[i][j] = 0

    print(sum(HW[H - 1]))


if __name__ == "__main__":
    main()
