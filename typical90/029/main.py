def main():
    W, N = map(int, input().split())

    LR = []
    T = set()
    for _ in range(N):
        L, R = map(int, input().split())
        LR.append((L, R))

        T.add(L)
        T.add(R)

    # 座標圧縮
    T = sorted(list(T))
    D = {v: i for i, v in enumerate(T)}
    H = [0 for _ in range(len(D))]

    for l, r in LR:
        ans = 0

        ll, rr = D[l], D[r]
        m = 0
        for i in range(ll, rr + 1):
            m = max(m, H[i])
        for i in range(ll, rr + 1):
            H[i] = m + 1
        ans = m + 1

        print(ans)


if __name__ == "__main__":
    main()
