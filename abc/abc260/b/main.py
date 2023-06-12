def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    P = []
    for i in range(N):
        P.append((i + 1, A[i], B[i]))

    ans = []

    P.sort(key=lambda x: x[1] * 10000 - x[0])
    for _ in range(X):
        a = P.pop()
        ans.append(a[0])

    P.sort(key=lambda x: x[2] * 10000 - x[0])
    for _ in range(Y):
        a = P.pop()
        ans.append(a[0])

    P.sort(key=lambda x: (x[1] + x[2]) * 10000 - x[0])
    for _ in range(Z):
        a = P.pop()
        ans.append(a[0])

    for a in sorted(ans):
        print(a)


if __name__ == "__main__":
    main()
