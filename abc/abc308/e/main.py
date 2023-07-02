def mex(i, j, k):
    for n in range(3):
        if n not in (i, j, k):
            return n
    else:
        return 3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = input()

    E = []
    M = [[0, 0, 0] for _ in range(N + 1)]
    X = [[0, 0, 0] for _ in range(N + 1)]
    for i, s in enumerate(S, 1):
        for ii in range(3):
            M[i][ii] = M[i - 1][ii]
            X[i][ii] = X[i - 1][ii]

        if s == "M":
            M[i][A[i - 1]] += 1

        if s == "X":
            X[i][A[i - 1]] += 1

        if s == "E":
            E.append(i - 1)

    ans = 0
    for j in E:
        for mi in range(3):
            for xi in range(3):
                ans += mex(mi, A[j], xi) * M[j][mi] * (X[N][xi] - X[j][xi])

    print(ans)


if __name__ == "__main__":
    main()
