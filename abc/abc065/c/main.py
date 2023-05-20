def main():
    N, M = map(int, input().split())

    MOD = 1000000007

    if abs(N - M) > 1:
        print(0)
        return
    
    d = 1
    for i in reversed(range(1, N + 1)):
        d *= i % MOD
        d %= MOD

    a = 1
    for i in reversed(range(1, M +1)):
        a *= i % MOD
        a %= MOD

    ans = 2 if N == M else 1
    ans *= d
    ans %= MOD
    ans *= a
    ans %= MOD
    print(ans)



if __name__ == "__main__":
    main()