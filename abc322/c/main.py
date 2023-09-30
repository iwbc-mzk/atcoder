import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    for i in range(1, N + 1):
        j = bisect.bisect_left(A, i)
        n = A[j]
        print(n - i)


if __name__ == "__main__":
    main()
