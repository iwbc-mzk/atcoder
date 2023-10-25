def main():
    N = int(input())
    A = list(map(int, list(input())))
    B = list(map(int, list(input())))

    MOD = 998244353

    for i in range(N):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]

    a, b = 0, 0
    for i in range(N):
        a += A[N - 1 - i] * pow(10, i, MOD) % MOD
        b += B[N - 1 - i] * pow(10, i, MOD) % MOD

    ans = (a * b) % MOD
    print(ans)


if __name__ == "__main__":
    main()
