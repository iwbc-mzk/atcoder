import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    L = [list(input()) for _ in range(R)]

    q = deque()
    q.append((sx - 1, sy - 1, 0))
    visited = set()
    visited.add((sx - 1, sy - 1))

    while q:
        x, y, d = q.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            xx, yy = x + dx, y + dy
            if not (0 <= xx < C) or not (0 <= yy < R):
                continue

            if (xx, yy) in visited:
                continue

            if (xx, yy) == (gx - 1, gy - 1):
                print(d + 1)
                return

            if L[yy][xx] == "#":
                continue

            q.append((xx, yy, d + 1))
            visited.add((xx, yy))


if __name__ == "__main__":
    main()
