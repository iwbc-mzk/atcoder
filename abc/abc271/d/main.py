from collections import defaultdict

def main():
    N, S = map(int, input().split())
    AB = [tuple(map(int, input().split())) for _ in range(N)]

    # dp[n][s]: n番目までのカードで総和sが可能か
    dp = defaultdict(lambda: defaultdict(bool))
    dp[0][0] = True
    for n in range(N + 1):
        if n == 0:
            a, b = 0, 0
        else:
            a, b = AB[n-  1]

        for s in range(S + 1):
            if dp[n - 1][s - a]:
                dp[n][s] |= dp[n - 1][s - a]

            if dp[n - 1][s - b]:
                dp[n][s] |= dp[n - 1][s - b]

    if dp[N][S]:
        cur_s = S
        ans = []
        for n in reversed(range(1, N+1)):
            a, b = AB[n-1]
            if dp[n-1][cur_s - a]:
                ans.insert(0, "H")
                cur_s -= a
            elif dp[n-1][cur_s - b]:
                ans.insert(0, "T")
                cur_s -= b

        print("Yes")
        print("".join(ans))
    else:
        print("No")

if __name__ == "__main__":
    main()