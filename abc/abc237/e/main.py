import sys
from collections import defaultdict
import heapq

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    G = defaultdict(set)
    for _ in range(M):
        U, V = map(int, input().split())
        G[U].add(V)
        G[V].add(U)

    scores = [float("inf")] * N
    scores[0] = -H[0]
    visited = set()

    q = [(scores[0], 1)]
    while q:
        score, v = heapq.heappop(q)
        if v in visited:
            continue

        visited.add(v)

        for vv in G[v]:
            if vv in visited:
                continue

            if H[v - 1] - H[vv - 1] >= 0:
                new_score = score
            else:
                new_score = score + (H[vv - 1] - H[v - 1])
            if new_score < scores[vv - 1]:
                scores[vv - 1] = new_score
                heapq.heappush(q, (new_score, vv))

    scores = [-score - H[i] for i, score in enumerate(scores)]

    print(max(scores))


if __name__ == "__main__":
    main()
