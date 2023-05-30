from collections import deque


def main():
    N = int(input())
    T = list(map(int, input().split()))
    t_sum = sum(T)

    dp = [[False for _ in range(t_sum + 1)] for _ in range(N + 1)]
    dp[0][0] = True
    s = 0
    for i in range(1, N + 1):
        t = T[i - 1]
        for j in range(t_sum + 1):
            if j - t >= 0 and dp[i - 1][j - t]:
                dp[i][j] = True

            if dp[i - 1][j]:
                dp[i][j] = True

    ans = None
    j = (t_sum + 1) // 2
    while not ans:
        if dp[N][j]:
            ans = j
        j += 1

    print(ans)


if __name__ == "__main__":
    main()
