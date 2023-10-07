import sys

sys.setrecursionlimit(10**9)


def extGCD(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)

    # a = qb + r => rx + b(qx + y) = d
    q, r = a // b, a % b
    d, y, x = extGCD(b, r)
    y -= q * x

    return (d, x, y)


def main():
    N, X = map(int, input().split())
    T = list(map(int, input().split()))
    MOD = 998244353

    # dp[t]: 時刻tに曲が入れ替わる確率
    dp = [0 for _ in range(X + 1)]
    dp[0] = 1
    # 1/Nの逆元
    nr = extGCD(N, MOD)[1] % MOD
    for x in range(1, X + 1):
        for n in range(N):  # 時刻xまでに流れていた曲
            t = T[n]
            # 時刻x-tに曲nに入れ替わっている確率
            # 曲nに入れ替わるのは曲が入れ替わる確率の1/N
            p = dp[x - t] * nr if t <= x else 0
            dp[x] += p % MOD
        dp[x] %= MOD

    # 時刻X+0.5に曲0が流れるのは 時刻X-T0+1 ~ 時刻X に曲が入れ替わるとき
    # かつ時刻Xの曲入れ替わり時に曲0が流れる(1/N)
    v = max(0, X - T[0] + 1)
    ans = sum(dp[v:]) * nr % MOD
    print(ans)


if __name__ == "__main__":
    main()
