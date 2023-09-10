def main():
    N, X, Y = map(int, input().split())
    P, T = [], []
    for _ in range(N - 1):
        p, t = map(int, input().split())
        P.append(p)
        T.append(t)

    Q = int(input())

    S = None
    for _ in range(Q):
        q = int(input())

        t = q + X
        if t % P[0]:
            t += P[0] - t % P[0]
        t += T[0]

        if t % P[1]:
            t += P[1] - t % P[1]

        if not S:
            S = 0
            for i in range(2, N):
                if i != 2 and (t + S) % P[i - 1]:
                    S += P[i - 1] - t % P[i - 1]
                S += T[i - 1]

        t += Y + S

        print(t)


if __name__ == "__main__":
    main()
