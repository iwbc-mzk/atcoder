from math import log10, floor


def main():
    L, R = map(int, input().split())

    MOD = 10**9 + 7

    if 10**10 < L:
        l = floor(log10(L // 10**10) + 10)
    else:
        l = floor(log10(L))

    if 10**10 < R:
        r = floor(log10(R // 10**10) + 10)
    else:
        r = floor(log10(R))

    ans = 0
    if l == r:
        n = R - L + 1
        ans += (l + 1) * n * (L + R) // 2
        ans %= MOD
    else:
        for i in range(l, r + 1):
            if i == l:
                n = 10 ** (i + 1) - L
                ans += (i + 1) * n * (L + (10 ** (i + 1) - 1)) // 2 % MOD
            elif i == r:
                n = R - 10**i + 1
                ans += (i + 1) * n * (10**i + R) // 2 % MOD
            else:
                n = 10 ** (i + 1) - 10 ** (i)
                ans += (i + 1) * n * (10**i + (10 ** (i + 1) - 1)) // 2 % MOD
            ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
