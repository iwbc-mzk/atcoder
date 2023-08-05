def main():
    N = int(input())

    n = int(N**0.5)
    ans = 0

    for i in range(1, n + 1):
        ans += i * ((N // i) - (N // (i + 1)))

    for i in range(1, N // (n + 1) + 1):
        ans += N // i

    print(ans)


if __name__ == "__main__":
    main()
