def NAND(x, y):
    return 0 if x == y == 1 else 1


def main():
    N = int(input())
    S = input()

    dp = [[0, 0] for _ in range(N + 1)]
    for i in range(N):
        s = int(S[i])
        dp[i + 1][NAND(0, s)] += dp[i][0]
        dp[i + 1][NAND(1, s)] += dp[i][1]
        dp[i + 1][s] += 1

    ans = 0
    for _, v in dp:
        ans += v

    print(ans)


if __name__ == "__main__":
    main()
