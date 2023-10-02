import sys

sys.setrecursionlimit(10**9)


def mod_comb(n: int, k: int, mod: int, memo=None) -> int:
    if not memo:
        memo = [1]
        for i in range(n + 1):
            memo.append((memo[i - 1] * i) % mod)

    def extGCD(a: int, b: int) -> tuple[int, int]:
        if b == 0:
            return (1, 0)

        q, r = a // b, a % b
        y, x = extGCD(b, r)
        y -= q * x

        return (x, y)

    return memo[n] * extGCD(memo[n - k], mod)[0] * extGCD(memo[k], mod)[0]


def main():
    X, Y = map(int, input().split())
    MOD = 10**9 + 7

    F = [1]
    for i in range(1, X + 1):
        F.append((F[i - 1] * i) % MOD)

    ans = 0
    m1, m2 = X, 0
    while m1 >= 0:
        y = m1 * 2 + m2
        if y == Y:
            ans += mod_comb(m1 + m2, m1, MOD, F)
            ans %= MOD

        m1 -= 2
        m2 += 1

    print(ans % MOD)


if __name__ == "__main__":
    main()
