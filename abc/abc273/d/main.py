from collections import defaultdict
import bisect


def main():
    H, W, RS, CS = map(int, input().split())
    N = int(input())
    WALLS = [tuple(map(int, input().split())) for _ in range(N)]
    Q = int(input())

    RW = defaultdict(list)
    for r, c in sorted(WALLS):
        RW[r].append(c)

    CW = defaultdict(list)
    for r, c in sorted(WALLS, key=lambda x: (x[1], x[0])):
        CW[c].append(r)

    r, c = RS, CS
    for _ in range(Q):
        d, l = input().split()
        l = int(l)

        if d == "U":
            if c in CW:
                i = bisect.bisect_left(CW[c], r)
                if i == 0:
                    r = max(1, r - l)
                else:
                    r = max(CW[c][i - 1] + 1, r - l)
            else:
                r = max(1, r - l)
        elif d == "D":
            if c in CW:
                i = bisect.bisect_left(CW[c], r)
                if i == len(CW[c]):
                    r = min(H, r + l)
                else:
                    r = min(CW[c][i] - 1, r + l)
            else:
                r = min(H, r + l)
        elif d == "L":
            if r in RW:
                i = bisect.bisect_left(RW[r], c)
                if i == 0:
                    c = max(1, c - l)
                else:
                    c = max(RW[r][i - 1] + 1, c - l)
            else:
                c = max(1, c - l)
        elif d == "R":
            if r in RW:
                i = bisect.bisect_left(RW[r], c)
                if i == len(RW[r]):
                    c = min(W, c + l)
                else:
                    c = min(RW[r][i] - 1, c + l)
            else:
                c = min(W, c + l)

        print(r, c)


if __name__ == "__main__":
    main()
