def main():
    S = int(input())
    MOD = 10**9 + 7

    N = S // 3

    ans = 0
    for i in range(N):
        s = S - 3 * (i + 1) + i

        t1 = 1
        t2 = 1
        while s > 0 and i > 0:
            t1 *= s
            t2 *= i

            s -= 1
            i -= 1

        ans += (t1 // t2) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
