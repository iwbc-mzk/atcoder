import heapq


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    heap = [*A]
    heapq.heapify(heap)
    hs = set(A)

    ans = set()
    while len(ans) < K:
        v = heapq.heappop(heap)
        ans.add(v)
        for a in A:
            if v + a not in hs:
                heapq.heappush(heap, v + a)
                hs.add(v + a)

    print(max(ans))


if __name__ == "__main__":
    main()
