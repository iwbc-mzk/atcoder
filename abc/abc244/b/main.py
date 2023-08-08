import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    T = input()

    dxy = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    x, y = 0, 0
    d = 0
    for t in T:
        if t == "S":
            dx, dy = dxy[d]
            x += dx
            y += dy
        else:
            d = (d + 1) % 4

    print(x, y)


if __name__ == "__main__":
    main()
