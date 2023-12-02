import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    P = [list(input()) for _ in range(N)]

    total = 0
    row = []
    row_cum = []
    for p in P:
        b = 0
        b_cum = [0]
        for pc in p:
            b_cum.append(b_cum[-1])
            if pc == "B":
                b += 1
                b_cum[-1] += 1


        row.append(b)
        row_cum.append(b_cum)
        total += b

    col = []
    col_cum = []
    for c in range(N):
        b = 0
        b_cum = [0]
        for r in range(N):
            b_cum.append(b_cum[-1])
            if P[r][c] == "B":
                b += 1
                b_cum[-1] += 1

        col.append(b)
        col_cum.append(b_cum)

    cum = []
    for p in P:
        b_cum = []
        for pc in p:
            b_cum.append(b_cum[-1] if b_cum else 0)
            if pc == "B":
                b_cum[-1] += 1


        cum.append(b_cum)

    for r in range(1, N):
        for c in range(N):
            cum[r][c] += cum[r - 1][c]

    for _ in range(Q):
        A, B, C, D = map(int, input().split())

        a = A % N
        b = B % N
        c = C % N
        d = D % N

        ta = A - a
        tb = B - b
        tc = C + (N - c)
        td = D + (N - d)

        lc = (tc - ta) // N * (td - tb) // N

        ans = total * lc
        ans -= sum(row[:a]) * (td - tb) // N
        ans -= sum(row[c + 1 :]) * (td - tb) // N
        ans -= sum(col[:b]) * (tc - ta) // N
        ans -= sum(col[d + 1 :]) * (tc - ta) // N
            

        ans += cum[(A - 1) % N][(B - 1) % N]
        k = cum[(tc - 1) % N][(B - 1) % N]
        s = cum[C % N][(tb - 1) % N]
        ans += cum[(tc - 1) % N][(B - 1) % N] - cum[(C + 1) % N][(tb - 1) % N]
        ans += cum[ta % N][(D + 1) % N] - cum[(A - 1) % N][(td - 1) % N]
        ans += cum[(C + 1) % N][(D + 1) % N] - cum[(tc - 1) % N][(td - 1) % N]

        print(ans)


if __name__ == "__main__":
    main()
