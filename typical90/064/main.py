def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    B = []
    E = 0
    for i in range(N - 1):
        B.append(A[i + 1] - A[i])
        E += abs(B[-1])

    for _ in range(Q):
        L, R, V = map(int, input().split())
        L, R = L - 1, R - 1

        if 0 < L:
            E -= abs(B[L - 1])
            B[L - 1] += V
            E += abs(B[L - 1])

        if R < N - 1:
            E -= abs(B[R])
            B[R] -= V
            E += abs(B[R])

        print(E)


if __name__ == "__main__":
    main()
