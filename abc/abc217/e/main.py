import sys
import heapq
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    Q = int(input())

    A = []
    B = deque()
    for _ in range(Q):
        i, *x = map(int, input().split())
        if i == 1:
            x = x[0]
            B.append(x)
        elif i == 2:
            if A:
                a = heapq.heappop(A)
                print(a)
            else:
                b = B.popleft()
                print(b)
        else:
            while B:
                b = B.popleft()
                heapq.heappush(A, b)


if __name__ == "__main__":
    main()
