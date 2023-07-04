def main():
    N = int(input())
    A = list(map(int, input().split()))

    A = [a for a in reversed(A)]
    p = 0 if A[0] < 4 else 1
    for i in range(1, N):
        A[i] += A[i - 1]
        if A[i] >= 4:
            p += 1

    print(p)


if __name__ == "__main__":
    main()
