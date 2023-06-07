def main():
    N = int(input())

    ans = 0
    for n in range(1, N + 1):
        i = N // n
        s = i * (2 * n + (i - 1) * n) // 2
        ans += s

    print(ans)


if __name__ == "__main__":
    main()
