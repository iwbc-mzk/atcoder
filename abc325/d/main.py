import sys
import heapq
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    TD = [tuple(map(int, input().split())) for _ in range(N)]
    TD = [(t, t + d) for t, d in TD]
    TD.sort(key=lambda x: (x[1], x[0]))

    ans = 0
    now = 0

    print(ans)


if __name__ == "__main__":
    main()
