import heapq


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    ans = [-1] * (K + 1)
    Q = []
    heapq.heappush(Q, 0)
    for i in range(K + 1):
        v = heapq.heappop(Q)
        if i >= 1 and ans[i - 1] == v:
            while v == ans[i - 1]:
                v = heapq.heappop(Q)
        ans[i] = v

        for j in range(N):
            heapq.heappush(Q, v + A[j])

    print(ans[K])


if __name__ == "__main__":
    main()
