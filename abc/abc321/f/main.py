import sys

sys.setrecursionlimit(10**9)


def main():
    Q, K = map(int, input().split())

    D = {}
    cnt = 0
    for _ in range(Q):
        i, x = input().split()
        x = int(x)
        if i == "+":
            if x in D:
                D[x] += 1
            else:
                D[x] = 1
            cnt += 1
        else:
            D[x] -= 1
            if D[x] == 0:
                del D[x]
            cnt -= 1

        dp = [[0 for _ in range(K + 1)] for _ in range(cnt + 1)]
        dp[0][0] = 1
        i = 1
        for v, c  in D.items():
            for _ in range(c):
                for k in range(1, K + 1):
                    if k - v >= 0:
                        dp[i][k] = dp[i - 1][k - v]
                i += 1
        print(dp[cnt][K])


if __name__ == "__main__":
    main()
