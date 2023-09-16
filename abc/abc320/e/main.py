import sys
import heapq

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    ans = [0 for _ in range(N)]
    INF = float("inf")

    H = list(range(N))
    heapq.heapify(H)
    event = []
    for _ in range(M):
        T, W, S = map(int, input().split())
        event.append((T, INF, W, S))

    while event:
        t, i, w, s = heapq.heappop(event)
        if i == INF:
            if H:
                h = heapq.heappop(H)
                heapq.heappush(event, (t + s, h, -1, -1))
                ans[h] += w
        else:
            heapq.heappush(H, i)

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
