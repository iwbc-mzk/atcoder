import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    H, W = map(int, input().split())
    S = [list(input()) for _ in range(H)]

    censor = set()
    for h in range(H):
        for w in range(W):
            if S[h][w] == "#":
                censor.add((h, w))

    fin = set()
    ans = 0
    for h, w in censor:
        if (h, w) in fin:
            continue

        q = deque()
        q.append((h, w))
        fin.add((h, w))
        while q:
            vh, vw = q.popleft()
            for dh, dw in [
                (1, 0),
                (1, 1),
                (0, 1),
                (-1, 1),
                (-1, 0),
                (-1, -1),
                (0, -1),
                (1, -1),
            ]:
                hh, ww = vh + dh, vw + dw
                if (hh, ww) not in fin and (hh, ww) in censor:
                    q.append((hh, ww))
                    fin.add((hh, ww))

        ans += 1

    print(ans)


if __name__ == "__main__":
    main()
