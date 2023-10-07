import sys
import heapq
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    S = []
    D = defaultdict(int)
    for _ in range(N):
        s, c = map(int, input().split())
        S.append(s)
        D[s] = c

    heapq.heapify(S)
    ans = 0
    while S:
        s = heapq.heappop(S)
        c = D[s]
        if c // 2 and 2 * s not in D:
            heapq.heappush(S, 2 * s)
        D[2 * s] += c // 2
        D[s] %= 2
        ans += D[s]

    print(ans)


if __name__ == "__main__":
    main()
