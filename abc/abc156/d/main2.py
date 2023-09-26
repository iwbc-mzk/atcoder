import sys

sys.setrecursionlimit(10**9)


# ax + by = gcd(a, b) = d となる d, x, yを返す
# mod P でのkの逆元計算はextGCD(P, k)のyになる
def extGCD(a: int, b: int) -> tuple[int, int, int]:
    if b == 0:
        return (a, 1, 0)

    # a = qb + r => rx + b(qx + y) = d
    q, r = a // b, a % b
    d, y, x = extGCD(b, r)
    y -= q * x

    return (d, x, y)


def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7

    AB = []
    for i in [A, B]:
        t = 1
        for j, v in enumerate(range(1, min(i, N - i) + 1)):
            t *= N - j
            t %= MOD

            inv = extGCD(MOD, v)[2]
            t *= inv
            t %= MOD

        t %= MOD
        AB.append(t)

    ans = (pow(2, N, MOD) - 1) % MOD - sum(AB)
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
