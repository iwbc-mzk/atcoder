import math
from collections import defaultdict


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A1 = A[:2]
    A2 = A[2:]
    A2.sort()

    ans = math.inf
    for i in range(N - 2):
        left = i
        right = i + M - 1
        if right >= N - 2:
            break

        c = 0
        if A2[left] < A1[0]:
            c += A1[0] - A2[left]
        if A2[right] > A1[1]:
            c += A2[right] - A1[1]

        ans = min(ans, c)

    print(ans)


if __name__ == "__main__":
    main()
