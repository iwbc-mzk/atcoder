import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    ans = 0
    for i, a in enumerate(A):
        j = bisect.bisect_left(A, a + M)
        ans = max(ans, j - i)

    print(ans)
    


if __name__ == "__main__":
    main()
