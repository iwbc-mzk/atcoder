from collections import defaultdict
import heapq


def main():
    N, M = map(int, input().split())
    H = list(map(int, input().split()))

    G = defaultdict(set)
    for _ in range(M):
        U, V = map(int, input().split())
        G[U].add(V)
        G[V].add(U)

    joyful = [0] * N
    joyful[0] = H[0]
    visited = set()

    q = [(-H[0], 1)]
    while q:
        joy, v = heapq.heappop(q)
        joy *= -1
        if v in visited:
            continue

        visited.add(v)

        for vv in G[v]:
            if vv in visited:
                continue

            if H[vv - 1] > H[v - 1]:
                new_joy = joy + 2 * (H[v - 1] - H[vv - 1])
            else:
                new_joy = joy + H[v - 1] - H[vv - 1]
            new_joy += H[vv - 1] - H[v - 1]

            if new_joy > joyful[vv - 1]:
                joyful[vv - 1] = new_joy
                heapq.heappush(q, (-new_joy, vv))

    joyful = [j - h for j, h in zip(joyful, H)]
    print(max(joyful))


if __name__ == "__main__":
    main()
