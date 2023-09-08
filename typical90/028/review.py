def main():
    N = int(input())

    M = 10**3
    P = [[0 for _ in range(M + 1)] for _ in range(M + 1)]

    for _ in range(N):
        lx, ly, rx, ry = map(int, input().split())
        P[lx][ly] += 1
        P[rx][ry] += 1
        P[rx][ly] -= 1
        P[lx][ry] -= 1

    for c in range(1, M + 1):
        for r in range(M + 1):
            P[r][c] += P[r][c - 1]

    for r in range(1, M + 1):
        for c in range(M + 1):
            P[r][c] += P[r - 1][c]

    ans = [0 for _ in range(N)]
    for c in range(M + 1):
        for r in range(M + 1):
            if P[r][c]:
                ans[P[r][c] - 1] += 1

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
