def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    idxs = {
        "r": 0,
        "p": 1,
        "s": 2
    }

    l = []
    i = 0
    flg = []
    while i < K:
        j = i
        while j < N:
            l.append(idxs[T[j]])
            flg.append(j != i)
            j += K

        i += 1

    dp = [[-1, -1, -1] for _ in range(N + 1)]
    dp[0] = [0, 0, 0]
    for i, (s, f) in enumerate(zip(l, flg), 1):
        if f:
            if s == 0:
                dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][2]) + P
                dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
            elif s == 1:
                dp[i][0] = max(dp[i - 1][1], dp[i - 1][2])
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
                dp[i][2] = max(dp[i - 1][0], dp[i - 1][1]) + S
            else:
                dp[i][0] = max(dp[i - 1][1], dp[i - 1][2]) + R
                dp[i][1] = max(dp[i - 1][0], dp[i - 1][2])
                dp[i][2] = max(dp[i - 1][0], dp[i - 1][1])
        else:
            m = max(dp[i - 1][0], dp[i - 1][1], dp[i - 1][2])
            if s == 0:
                dp[i] = [m, m + P, m]
            elif s == 1:
                dp[i] = [m, m, m + S]
            else:
                dp[i] = [m + R, m, m]

    print(max(dp[N]))

if __name__ == "__main__":
    main()