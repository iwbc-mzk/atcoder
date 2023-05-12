from collections import defaultdict

def main():
    s = input()
    t = input()

    dp = defaultdict(lambda: defaultdict(int))
    for i in range(1, len(s) + 1):
        s_idx = i - 1
        for j in range(1, len(t) + 1):
            t_idx = j - 1

            if s[s_idx] == t[t_idx]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    ans = []
    i = len(s)
    j = len(t)

    while len(ans) < dp[len(s)][len(t)]:
        if s[i - 1] == t[j - 1]:
            ans.insert(0, s[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i][j] == dp[i - 1][j]:
                i -= 1
            else: 
                j -= 1

    print("".join(ans))



if __name__ == "__main__":
    main()