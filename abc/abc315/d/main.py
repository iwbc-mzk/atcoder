def convert(s):
    return ord(s) - ord("a")


def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    rows = [[0] * 26 for _ in range(H)]
    cols = [[0] * 26 for _ in range(W)]
    for i in range(H):
        for j in range(W):
            s = C[i][j]
            rows[i][convert(s)] += 1
            cols[j][convert(s)] += 1

    HS = set(range(H))
    WS = set(range(W))
    while True:
        trh = set()
        trw = set()
        for h in HS:
            if len(WS) < 2:
                break

            flg = False
            for v in rows[h]:
                if v > 0:
                    if not flg:
                        flg = True
                    else:
                        break
            else:
                trh.add(h)

        for w in WS:
            if len(HS) < 2:
                break

            flg = False
            for v in cols[w]:
                if v > 0:
                    if not flg:
                        flg = True
                    else:
                        break
            else:
                trw.add(w)

        if not trh and not trw:
            break
        else:
            HS = HS.difference(trh)
            for t in trh:
                for w in range(W):
                    cols[w][convert(C[t][w])] -= 1

            WS = WS.difference(trw)
            for t in trw:
                for h in range(H):
                    rows[h][convert(C[h][t])] -= 1

    lh = H - len(HS)
    lw = W - len(WS)
    ans = H * W - W * lh - H * lw + lh * lw
    print(ans)


if __name__ == "__main__":
    main()
