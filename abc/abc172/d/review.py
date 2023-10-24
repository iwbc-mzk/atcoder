def main():
    N = int(input())
    F = [0 for _ in range(N)]

    # エラトステネスの篩のようにして各nの倍数のFに加算
    for n in range(1, N + 1):
        nn = n
        while nn <= N:
            F[nn - 1] += 1
            nn += n

    ans = 0
    for i, f in enumerate(F, 1):
        ans += i * f

    print(ans)


if __name__ == "__main__":
    main()
