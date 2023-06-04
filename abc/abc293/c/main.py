def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]

    ans = 0

    def rec(h: int, w: int, s: set):
        nonlocal ans

        a = A[h][w]

        s.add(a)
        if h == H - 1 and w == W - 1:
            s.remove(a)
            ans += 1
            return

        if h + 1 < H and A[h + 1][w] not in s:
            rec(h + 1, w, s)
        if w + 1 < W and A[h][w + 1] not in s:
            rec(h, w + 1, s)

        s.remove(a)

    rec(0, 0, set())
    print(ans)


if __name__ == "__main__":
    main()
