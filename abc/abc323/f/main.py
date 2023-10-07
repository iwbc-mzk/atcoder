import sys

sys.setrecursionlimit(10**9)


def main():
    XA, YA, XB, YB, XC, YC = map(int, input().split())
    dx, dy = XC - XB, YC - YB

    ans1 = 0
    if XB > XC:
        xa = XB + 1 - XA
    else:
        xa = XB - 1 - XA
    ya = abs(YB - YA)

    if YA == YB:
        xa += 4
    ans1 += xa
    ans1 += ya
    ans1 += abs(dy)
    ans1 += 3
    ans1 += abs(dx)

    ans2 = 0
    if YB > YC:
        ya = YB + 1 - YA
    else:
        ya = YB - 1 - YA
    xa = abs(XB - XA)
    if XA == XB:
        ya += 4
    ans2 += ya
    ans2 += xa
    ans2 += abs(dx)
    ans2 += 3
    ans2 += abs(dy)

    print(min(ans1, ans2))


if __name__ == "__main__":
    main()
