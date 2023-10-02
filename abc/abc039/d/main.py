import sys

sys.setrecursionlimit(10**9)

DHW = [
    (1, 0),
    (1, 1),
    (0, 1),
    (-1, 1),
    (-1, 0),
    (-1, -1),
    (0, -1),
    (1, -1),
]


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    ans = [["." for _ in range(W)] for _ in range(H)]
    valid = [["." for _ in range(W)] for _ in range(H)]
    for h in range(H):
        for w in range(W):
            if S[h][w] != "#":
                continue

            for dh, dw in DHW:
                hh, ww = h + dh, w + dw
                if not (0 <= hh < H) or not (0 <= ww < W):
                    continue
                if S[hh][ww] != "#":
                    break
            else:
                ans[h][w] = "#"
                valid[h][w] = "#"
                for dh, dw in DHW:
                    hh, ww = h + dh, w + dw
                    if not (0 <= hh < H) or not (0 <= ww < W):
                        continue
                    else:
                        valid[hh][ww] = "#"

    if S != valid:
        print("impossible")
    else:
        print("possible")
        for a in ans:
            print("".join(a))


if __name__ == "__main__":
    main()
