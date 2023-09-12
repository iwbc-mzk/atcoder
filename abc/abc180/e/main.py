def main():
    N = int(input())
    XYZ = [list(map(int, input().split())) for _ in range(N)]

    W = {key1: {key2: 0 for key2 in range(N)} for key1 in range(N)}
    for i, (a, b, c) in enumerate(XYZ):
        for j, (p, q, r) in enumerate(XYZ):
            W[i][j] = abs(p - a) + abs(q - b) + max(0, r - c)
            W[j][i] = abs(a - p) + abs(b - q) + max(0, c - r)

    # dp[S][i]: 現在地が都市iで訪問済の町の集合がSであるときのコストの最小値
    INF = float("inf")
    dp = [[INF for _ in range(N)] for _ in range(1 << N)]
    dp[1][0] = 0

    for bit in range(1 << N):
        for v in range(N):
            # 都市v(移動元)が未訪問はスキップ
            if not (bit & (1 << v)):
                continue

            for nv in range(N):
                # 今回は三角不等式が成り立つので、全ての都市は1度のみ通る
                # => 都市nv(移動先)が訪問済はスキップ
                if bit & (1 << nv):
                    continue

                nbit = bit | (1 << nv)
                dp[nbit][nv] = min(dp[nbit][nv], dp[bit][v] + W[v][nv])

    ans = float("inf")
    for v in range(N):
        # 現在地が都市vで全都市訪問済(dp[v][(1<<N) - 1])の状態から都市1に戻る
        # => 最小値が答え
        ans = min(ans, dp[(1 << N) - 1][v] + W[v][0])

    print(ans)


if __name__ == "__main__":
    main()
