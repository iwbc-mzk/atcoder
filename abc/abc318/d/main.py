import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    D = [list(map(int, input().split())) for _ in range(N - 1)]

    G = defaultdict(lambda: defaultdict(int))
    for i in range(N - 1):
        for j in range(i + 1, N):
            G[i][j] = D[i][j - i - 1]
            G[j][i] = D[i][j - i - 1]

    dp = [0 for _ in range(2**N)]
    for b in range(2**N - 1):
        # 未確定頂点を1つ特定
        l = -1
        for i in range(N):
            if not (b >> i & 1):
                l = i
                break

        # もう一方の頂点毎に遷移を計算
        for j in range(N):
            if not (b >> j & 1):
                nb = b | (1 << l) | (1 << j)
                dp[nb] = max(dp[nb], dp[b] + G[l][j])

    print(dp[2**N - 1])


if __name__ == "__main__":
    main()
