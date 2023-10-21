import sys
import heapq
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    TD = [tuple(map(int, input().split())) for _ in range(N)]
    TD = [(t, t + d) for t, d in TD]
    TD.sort()
    TD = deque(TD)

    ans = 0
    now = 0
    pq = []
    for _ in range(N):
        if not pq and TD:
            now = TD[0][0]

        while TD and TD[0][0] == now:
            t, td = TD.popleft()
            heapq.heappush(pq, (td, t))

        while pq:
            td, t = heapq.heappop(pq)
            if t <= now <= td:
                ans += 1
                now += 1
                break

    print(ans)


if __name__ == "__main__":
    main()
