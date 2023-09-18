import sys

sys.setrecursionlimit(10**9)

D = {
    "R": (1, 0),
    "L": (-1, 0),
    "U": (0, -1),
    "D": (0, 1),
    "RU": (1, -1),
    "RD": (1, 1),
    "LU": (-1, -1),
    "LD": (-1, 1),
}


def main():
    X, Y, W = input().split()
    X, Y = int(X), int(Y)

    C = [list(input()) for _ in range(9)]

    x, y = X - 1, Y - 1
    dx, dy = D[W]
    ans = []
    while len(ans) < 4:
        ans.append(C[y][x])

        if not (0 <= x + dx <= 8):
            dx = -dx
        x += dx

        if not (0 <= y + dy <= 8):
            dy = -dy
        y += dy

    print("".join(ans))


if __name__ == "__main__":
    main()
