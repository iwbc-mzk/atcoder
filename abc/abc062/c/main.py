import sys

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())

    if H % 3 == 0 or W % 3 == 0:
        print(0)
        return

    ans = float("inf")

    # H分割
    u, d = 0, H
    while d - u > 1:
        m = (u + d) // 2

        if m * W * 2 < (H - m) * W:
            u = m
        else:
            d = m

    for h in [u, d]:
        s1 = h * W
        # W分割
        for wm in [W // 2, W // 2 + 1]:
            s2 = (H - h) * wm
            s3 = (H - h) * (W - wm)

            diff = max(s1, s2, s3) - min(s1, s2, s3)
            if diff < ans:
                ans = diff
        # H分割
        h_half = (H - h) // 2
        for hm in [h_half, h_half + 1]:
            s2 = hm * W
            s3 = (H - h - hm) * W

            diff = max(s1, s2, s3) - min(s1, s2, s3)
            if diff < ans:
                ans = diff

    # W分割
    l, r = 0, W
    while r - l > 1:
        m = (l + r) // 2

        if m * h * 2 < (W - m) * h:
            l = m
        else:
            r = m

    for w in [l, r]:
        s1 = H * w
        # H分割
        for hm in [H // 2, H // 2 + 1]:
            s2 = hm * (W - w)
            s3 = (H - hm) * (W - w)

            diff = max(s1, s2, s3) - min(s1, s2, s3)
            if diff < ans:
                ans = diff

        # W分割
        w_half = (W - w) // 2
        for wm in [w_half, w_half + 1]:
            s2 = H * wm
            s3 = H * (W - w - wm)

            diff = max(s1, s2, s3) - min(s1, s2, s3)
            if diff < ans:
                ans = diff

    print(ans)


if __name__ == "__main__":
    main()
