import sys

sys.setrecursionlimit(10**9)


def pow(x, n, mod):
    if n == 0:
        return 1
    elif n % 2:
        return (x * (pow(x, n - 1, mod) % mod)) % mod
    else:
        return ((pow(x, n // 2, mod) % mod) ** 2) % mod


def main():
    N, K = map(int, input().split())

    MOD = 10**9 + 7

    ans = 1
    ans *= K % MOD
    ans %= MOD

    if N == 1:
        print(ans)
        return

    ans *= (K - 1) % MOD
    ans %= MOD

    if N == 2:
        print(ans)
        return

    ans *= pow(K - 2, N - 2, MOD)
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
