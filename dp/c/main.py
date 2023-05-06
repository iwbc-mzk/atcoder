from collections import defaultdict

def main():
    N = int(input())

    dp = defaultdict(lambda: defaultdict(int))
    dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0 
    for n in range(1, N + 1):
        a, b, c = map(int, input().split())
        # a
        dp[n][0] = max(dp[n][0], dp[n - 1][1] + a, dp[n - 1][2] + a)
        # b
        dp[n][1] = max(dp[n][1], dp[n - 1][0] + b, dp[n - 1][2] + b)
        # c
        dp[n][2] = max(dp[n][2], dp[n - 1][0] + c, dp[n - 1][1] + c)

    print(max(dp[N].values()))



if __name__ == "__main__":
    main()