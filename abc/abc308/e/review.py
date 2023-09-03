def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = input()

    M0, M1, M2, X0, X1, X2 = [0], [0], [0], [0], [0], [0]
    E0, E1, E2 = [], [], []
    for i, (s, a) in enumerate(zip(S, A), 1):
        M0.append(M0[-1])
        M1.append(M1[-1])
        M2.append(M2[-1])
        X0.append(X0[-1])
        X1.append(X1[-1])
        X2.append(X2[-1])
        if s == "M":
            if a == 0:
                M0[-1] += 1
            elif a == 1:
                M1[-1] += 1
            else:
                M2[-1] += 1
        elif s == "X":
            if a == 0:
                X0[-1] += 1
            elif a == 1:
                X1[-1] += 1
            else:
                X2[-1] += 1
        else:
            if a == 0:
                E0.append(i)
            elif a == 1:
                E1.append(i)
            else:
                E2.append(i)

    M = [M0, M1, M2]
    E = [E0, E1, E2]
    X = [X0, X1, X2]

    ans = 0
    for mi in range(3):
        for ei in range(3):
            for xi in range(3):
                for e in E[ei]:
                    s = set([0, 1, 2, 3])
                    s.discard(mi)
                    s.discard(ei)
                    s.discard(xi)
                    v = min(s)

                    ans += v * M[mi][e] * (X[xi][-1] - X[xi][e])

    print(ans)


if __name__ == "__main__":
    main()
