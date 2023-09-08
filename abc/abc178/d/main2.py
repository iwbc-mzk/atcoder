def main():
    S = int(input())
    MOD = 10**9 + 7

    # dp[n]: S=nの時の数列の個数
    dp = [0 for _ in range(S + 1)]
    dp[0] = 1
    
    for s in range(1, S + 1):
        # 新たに追加する項は 0 ~ s-3 のいずれか
        # => 遷移元は s-3, s-4,..., 1, 0
        for i in range(s - 2):
            dp[s] += dp[i]

        dp[s] %= MOD

    print(dp[S])


if __name__ == "__main__":
    main()
