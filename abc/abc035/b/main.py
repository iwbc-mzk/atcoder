import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()
    T = int(input())

    dx, dy = 0, 0
    t = 0
    for s in S:
        if s == "L":
            dx -= 1
        elif s == "R":
            dx += 1
        elif s == "U":
            dy += 1
        elif s == "D":
            dy -= 1
        else:
            t += 1

    dx = abs(dx)
    dy = abs(dy)

    if T == 1:
        ans = dx + dy + t
    else:
        if dx + dy < t:
            ans = abs(dx + dy - t) % 2
        else:
            ans = abs(dx + dy - t)

    print(ans)


if __name__ == "__main__":
    main()
