def main():
    N = int(input())

    ans = 0
    for i in range(1, N + 1):
        j = i

        d = 2
        while d * d <= j:
            while j % (d * d) == 0:
                j /= d * d
            d += 1

        k = 1
        while k * k * j <= N:
            ans += 1
            k += 1

    print(ans)


if __name__ == "__main__":
    main()
