def main():
    N = int(input())

    MOD = 10**9 + 7

    total = 10**N % MOD
    no_zero = 9**N % MOD
    no_nine = no_zero
    no_zero_nine = 8**N % MOD

    ans = total - no_zero - no_nine + no_zero_nine
    ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
