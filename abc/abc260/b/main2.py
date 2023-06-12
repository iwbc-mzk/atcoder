def main():
    N, X, Y, Z = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    P = []
    for i in range(N):
        P.append((i + 1, A[i], B[i]))

    ans = []

    P.sort(key=lambda x: (x[1], -x[0]), reverse=True)
    P[X:] = sorted(P[X:], key=lambda x: (x[2], -x[0]), reverse=True)
    P[X + Y:] = sorted(P[X + Y:], key=lambda x: (x[1] + x[2], -x[0]), reverse=True)
    P[:X + Y + Z] = sorted(P[:X + Y + Z], key=lambda x: x[0])

    for p in P[:X + Y + Z]:
        print(p[0])


if __name__ == "__main__":
    main()
