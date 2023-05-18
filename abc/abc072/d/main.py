def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = 0
    i = 0
    while i < N:
        if P[i] == i + 1:
            if i + 1 < N and P[i + 1] == i + 2:
                ans += 1
                i += 2
            else:
                ans += 1
                i += 2
        else:
            i += 1

    print(ans)
                


if __name__ == "__main__":
    main()