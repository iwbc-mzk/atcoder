from collections import defaultdict
import heapq
import math


def main():
    N, M, K = map(int, input().split())
    gragh = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        gragh[a].add(b)
        gragh[b].add(a)

    PH = defaultdict(int)
    heap = []
    for _ in range(K):
        p, h = map(int, input().split())
        PH[p] = h
        heap.append((-h, p))

    heapq.heapify(heap)

    ans = [(PH[i] if i in PH else -math.inf) for i in range(1, N + 1)]
    while heap:
        h, p = heapq.heappop(heap)
        h = -h

        for pp in gragh[p]:
            if ans[pp - 1] < h - 1:
                ans[pp - 1] = h - 1
                heapq.heappush(heap, (-(h - 1), pp))

    cnt = 0
    ans_idx = []
    for i, a in enumerate(ans):
        if a >= 0:
            cnt += 1
            ans_idx.append(i + 1)
    print(cnt)
    print(*ans_idx)


if __name__ == "__main__":
    main()
