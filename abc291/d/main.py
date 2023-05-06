from collections import defaultdict

MOD = 998244353

def main():
    N = int(input())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    # n枚目のカードまででn枚目が表/裏の時、条件を満たす場合の数
    dp = defaultdict(lambda: defaultdict(int))
    dp[1] = [1, 1]
    for n in range(2, N + 1):
        for b in range(2):
            for pre_b in range(2):
                if AB[n - 1][b] != AB[n - 2][pre_b]:
                    dp[n][b] += dp[n - 1][pre_b]
        dp[n][0] %= MOD
        dp[n][1] %= MOD


    print((dp[N][0] + dp[N][1]) % MOD)

if __name__ == "__main__":
    main()