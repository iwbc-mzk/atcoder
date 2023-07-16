from collections import defaultdict


def main():
    N = int(input())

    max_rx, max_ry = 0, 0
    S = []
    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        S.append((lx, ly, rx, ry))
        max_rx = max(max_rx, rx)
        max_ry = max(max_ry, ry)

    D = [[0 for _ in range(max_ry + 1)] for _ in range(max_rx + 1)]
    for lx, ly, rx, ry in S:
        D[lx][ly] += 1
        D[rx][ry] += 1
        D[lx][ry] -= 1
        D[rx][ly] -= 1

    # 列方向累積和
    for c in range(max_rx + 1):
        for r in range(1, max_ry + 1):
            D[c][r] += D[c][r - 1]

    # 行方向累積和
    for r in range(max_ry + 1):
        for c in range(1, max_rx + 1):
            D[c][r] += D[c - 1][r]

    ans = defaultdict(int)
    for r in D:
        for c in r:
            ans[c] += 1

    for i in range(1, N + 1):
        print(ans[i])


if __name__ == "__main__":
    main()
