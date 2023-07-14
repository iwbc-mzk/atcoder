import math
import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())
    B = [int(input()) for _ in range(Q)]

    A.sort()
    for b in B:
        i = bisect.bisect_left(A, b)
        ans = math.inf

        if i < N:
            ans = min(ans, abs(A[i] - b))
        if i + 1 < N:
            ans = min(ans, abs(A[i + 1] - b))
        if 0 <= i - 1 < N:
            ans = min(ans, abs(A[i - 1] - b))

        print(ans)


if __name__ == "__main__":
    main()
