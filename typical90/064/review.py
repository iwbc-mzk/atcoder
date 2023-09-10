def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    E = 0
    H = []
    for i in range(N - 1):
        E += abs(A[i + 1] - A[i])
        H.append([A[i], A[i + 1], A[i + 1] - A[i]])

    for _ in range(Q):
        L, R, V = map(int, input().split())
        if L != 1:
            E -= abs(H[L - 2][2])
            H[L - 2][1] += V
            H[L - 2][2] = H[L - 2][1] - H[L - 2][0]
            E += abs(H[L - 2][2])

        if R != N:
            E -= abs(H[R - 1][2])
            H[R - 1][0] += V
            H[R - 1][2] = H[R - 1][1] - H[R - 1][0]
            E += abs(H[R - 1][2])

        print(E)


if __name__ == "__main__":
    main()
