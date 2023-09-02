def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = []
    a = A[0]
    for i in range(1, N):
        if i % 2:
            a -= A[i]
        else:
            a += A[i]

    x1 = a
    ans.append(x1)

    p = ans[-1] // 2
    for i in range(N - 1):
        ans.append((A[i] - p) * 2)
        p = ans[-1] // 2

    print(*ans)


if __name__ == "__main__":
    main()
