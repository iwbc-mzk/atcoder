from math import ceil


def main():
    N, P = map(int, input().split())
    MOD = 998244353

    K = [1, 1]
    invK = [1, 1]
    inv = [None, 1]
    for i in range(2, max(101, N + 1)):
        K.append((K[i - 1] * i) % MOD)
        inv.append(MOD - inv[MOD % i] * (MOD // i) % MOD)
        invK.append(invK[i - 1] * inv[i] % MOD)

    def calc(i):
        n = N - i
        m = ceil(n / 2)
        if i + 2 * m > N and i > 0:
            t = i + m - 1
        else:
            t = i + m
        return (
            (i + m)
            * (K[t] * invK[t - i] * invK[i])
            * pow(100 - P, i, MOD)
            * pow(P, m, MOD)
            * pow(inv[100], (i + m), MOD)
        ) % MOD

    ans = 0
    for i in range(N + 1):
        ans += calc(i)
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
