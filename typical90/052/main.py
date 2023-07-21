def main():
    N = int(input())

    MOD = 10**9 + 7

    ans = 1
    for _ in range(N):
        A = list(map(int, input().split()))
        ans *= sum(A) % MOD
        ans %= MOD

    print(ans)


if __name__ == "__main__":
    main()
