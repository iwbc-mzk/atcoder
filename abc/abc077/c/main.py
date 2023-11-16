import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    B = sorted(map(int, input().split()))
    C = sorted(map(int, input().split()))

    ans = 0
    for b in B:
        ai = bisect.bisect_left(A, b)
        ci = bisect.bisect_right(C, b)

        ans += ai * (N - ci)

    print(ans)


if __name__ == "__main__":
    main()
