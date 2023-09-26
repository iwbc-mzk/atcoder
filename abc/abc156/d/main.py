import sys

sys.setrecursionlimit(10**9)


def main():
    N, A, B = map(int, input().split())
    MOD = 10**9 + 7

    AB = []
    for i in [A, B]:
        t1, t2 = 1, 1
        for j, v in enumerate(range(1, min(i, N - i) + 1)):
            t1 *= N - j
            t1 %= MOD

            t2 *= v
            t2 %= MOD

        t = t1 * pow(t2, MOD - 2, MOD)
        t %= MOD
        AB.append(t)

    ans = (pow(2, N, MOD) - 1) % MOD - sum(AB)
    ans %= MOD
    print(ans)


if __name__ == "__main__":
    main()
