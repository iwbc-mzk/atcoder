def main():
    N = int(input())
    A = list(map(int, input().split()))

    s = 0
    ans = []
    for i in range(7 * N):
        s += A[i]
        if i % 7 == 6:
            ans.append(s)
            s = 0

    print(*ans)


if __name__ == "__main__":
    main()
