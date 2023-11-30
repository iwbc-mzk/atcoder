def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = float("inf")

    dp1 = [[0, 0] for _ in range(N + 1)]
    dp1[1] = [float("inf"), A[0]]
    for n in range(2, N + 1):
        dp1[n][0] = dp1[n - 1][1]
        dp1[n][1] = min(dp1[n - 1]) + A[n - 1]

    ans = min(ans, min(dp1[N]))

    dp2 = [[0, 0] for _ in range(N + 1)]
    dp2[1] = [0, float("inf")]
    for n in range(2, N + 1):
        dp2[n][0] = dp2[n - 1][1]
        dp2[n][1] = min(dp2[n - 1]) + A[n - 1]

    ans = min(ans, dp2[N][1])

    print(ans)


if __name__ == "__main__":
    main()
