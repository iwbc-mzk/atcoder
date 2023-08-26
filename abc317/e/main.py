import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())
    A = [list(input()) for _ in range(H)]

    s = None
    g = None

    for h in range(H):
        for w in range(W):
            if A[h][w] == "S":
                s = (h, w)
                continue
            if A[h][w] == "G":
                g = (h, w)
                continue

            if A[h][w] in [".", "#"]:
                continue

            if A[h][w] == ">":
                dh, dw = 0, 1
            elif A[h][w] == "<":
                dh, dw = 0, -1
            elif A[h][w] == "^":
                dh, dw = -1, 0
            else:
                dh, dw = 1, 0

            A[h][w] = "#"
            hh, ww = h + dh, w + dw
            while 0 <= hh < H and 0 <= ww < W:
                if A[hh][ww] == ".":
                    A[hh][ww] = "#"
                    hh += dh
                    ww += dw
                else:
                    break

    ans = -1
    visited = set()
    visited.add(s)
    q = deque()
    q.append((s[0], s[1], 0))
    while q:
        h, w, d = q.popleft()
        if (h, w) == g:
            ans = d
            break

        for dh, dw in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            hh, ww = h + dh, w + dw
            if not (0 <= hh < H) or not (0 <= ww < W):
                continue

            if (hh, ww) in visited:
                continue

            if A[hh][ww] == "#":
                continue

            q.append((hh, ww, d + 1))
            visited.add((hh, ww))

    print(ans)


if __name__ == "__main__":
    main()
