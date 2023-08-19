def main():
    H, W = map(int, input().split())
    C = [input() for _ in range(H)]

    HS = set(range(H))
    WS = set(range(W))
    while True:
        trh = set()
        trw = set()
        for h in HS:
            if len(WS) < 2:
                break

            s = None
            for w in WS:
                if s is None:
                    s = C[h][w]
                else:
                    if s == C[h][w]:
                        continue
                    else:
                        break
            else:
                trh.add(h)

        for w in WS:
            if len(HS) < 2:
                break

            s = None
            for h in HS:
                if s is None:
                    s = C[h][w]
                else:
                    if s == C[h][w]:
                        continue
                    else:
                        break
            else:
                trw.add(w)

        if not trh and not trw:
            break
        else:
            HS = HS.difference(trh)
            WS = WS.difference(trw)

    lh = H - len(HS)
    lw = W - len(WS)
    ans = H * W - W * lh - H * lw + lh * lw
    print(ans)


if __name__ == "__main__":
    main()
