import sys

sys.setrecursionlimit(10**9)


def calc(a, b):
    return a**3 + a**2 * b + a * b**2 + b**3


def main():
    N = int(input())

    ans = float("inf")
    for a in range(0, 10**6 + 1):
        if a > N:
            break

        l, r = -1, 10**6 + 1
        while r - l > 1:
            mid = (l + r) // 2
            v = calc(a, mid)
            if v >= N:
                r = mid
            else:
                l = mid

        ans = min(ans, calc(a, r))

    print(ans)


if __name__ == "__main__":
    main()
