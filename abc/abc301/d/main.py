
def main():
    S = input()
    N = int(input())

    dp = [[-1, -1] for _ in range(len(S) + 1)]
    dp[0] = 0, 0
    
    for i, s in enumerate(S, 1):
        if s == "0":
            t = -1
            for j in [0, 1]:
                if dp[i - 1][j] >= 0:
                    t = max(t, dp[i - 1][j])
            dp[i][0] = t if t >= 0 else -1
        elif s == "1":
            t = -1
            for j in [0, 1]:
                if dp[i - 1][j] >= 0 and dp[i - 1][j] + 2 ** (i - 1) <= N:
                    t = max(t, dp[i - 1][j] + 2 ** (i - 1))
            dp[i][1] = t if t >= 0 else -1
        else:
            t = -1
            for j in [0, 1]:
                if dp[i - 1][j] >= 0:
                    t = max(t, dp[i - 1][j])
            dp[i][0] = t if t >= 0 else -1

            t = -1
            for j in [0, 1]:
                if dp[i - 1][j] >= 0 and dp[i - 1][j] + 2 ** (i - 1) <= N:
                    t = max(t, dp[i - 1][j] + 2 ** (i - 1))
            dp[i][1] = t if t >= 0 else -1

    for s, (i, j) in zip(S, reversed(dp)):
        if s != "?":
            if s == "1" and i >= 0 and i <= N:
                print(i)
                break
            if s == "0" and j >= 0 and j <= N:
                print(j)
                break
        else:
            if i > j and i >= 0 and i <= N:
                print(i)
                break
            if j > i and j >= 0 and j <= N:
                print(j)
                break
    else:
        print(-1)


if __name__ == "__main__":
    main()