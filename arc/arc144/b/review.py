from math import ceil


def main():
    N, a, b = map(int, input().split())
    A = list(map(int, input().split()))

    l, r = 0, max(A) + 1
    while r - l > 1:
        m = (l + r) // 2

        ac = 0
        bc = 0
        for v in A:
            if v < m:
                ac += ceil((m - v) / a)
            elif v > 0:
                bc += (v - m) // b

        if ac <= bc:
            l = m
        else:
            r = m

    print(l)


if __name__ == "__main__":
    main()
