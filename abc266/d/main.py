from collections import defaultdict

def main():
    N = int(input())
    X = defaultdict(int)
    A = defaultdict(int)
    for _ in range(N):
        t, x, a = map(int, input().split())
        X[t] = x
        A[t] = a

    t_max = 10 ** 5

    # dp[t][x]: 時刻t, 位置xの時のAの最大合計値
    init_val = -1
    dp = defaultdict(lambda: defaultdict(lambda: -1))
    dp[0][0] = 0
    for t in range(1, t_max + 1):
        for x in range(5):
            dp[t][x] = dp[t - 1][x]
            if x > 0:
                dp[t][x] = max(dp[t][x], dp[t - 1][x - 1])
            if x < 4:
                dp[t][x] = max(dp[t][x], dp[t - 1][x + 1])
        if dp[t][X[t]] != init_val:
            dp[t][X[t]] += A[t]

    print(max(dp[t_max][x] for x in range(5)))



if __name__ == "__main__":
    main()