def calc(L, X, Y):
    res = 0
    l, r = 0, 0
    cx, cy = 0, 0
    while l < len(L):
        while r < len(L) and not (cx != 0 and cy != 0):
            if L[r] == X:
                cx += 1
            if L[r] == Y:
                cy += 1
            r += 1

        if cx > 0 and cy > 0:
            res += len(L) - (r - 1)
        if L[l] == X:
            cx -= 1
        if L[l] == Y:
            cy -= 1
        l += 1

    return res


def main():
    N, X, Y = map(int, input().split())
    A = list(map(int, input().split()))

    AA = []
    ans = 0
    for a in A:
        if Y <= a <= X:
            AA.append(a)
        elif AA:
            ans += calc(AA, X, Y)
            AA = []
    else:
        ans += calc(AA, X, Y)

    print(ans)


if __name__ == "__main__":
    main()
