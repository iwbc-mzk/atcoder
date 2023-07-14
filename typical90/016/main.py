def main():
    N = int(input())
    A, B, C = map(int, input().split())

    coins = [A, B, C]
    coins.sort(reverse=True)

    ans = 10**4

    i = N // coins[0]
    if N % coins[0] == 0:
        ans = min(ans, i)

    while i >= 0:
        i_remain = N - coins[0] * i

        j = i_remain // coins[1]
        if i_remain % coins[1] == 0:
            ans = min(ans, i + j)

        while j >= 0:
            j_remain = i_remain - coins[1] * j

            k = j_remain // coins[2]
            if j_remain % coins[2] == 0:
                ans = min(ans, i + j + k)

            j -= 1

        i -= 1

    print(ans)


if __name__ == "__main__":
    main()
