from collections import defaultdict

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    dp = defaultdict(int)
    dp[0] = 0
    for n in range(N + 1):
        for a in A:
            if a <= n:
                dp[n] = max(dp[n], a + (n - a) - dp[n - a])

    print(dp[N])



if __name__ == "__main__":
    main()