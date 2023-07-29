import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    left = 0
    right = 10**9 + 1
    while right - left > 1:
        mid = (left + right) // 2
        a = bisect.bisect_right(A, mid)

        b = len(B) - bisect.bisect_left(B, mid)
        if a >= b:
            right = mid
        else:
            left = mid

    print(right)


if __name__ == "__main__":
    main()
