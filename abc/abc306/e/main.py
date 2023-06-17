import heapq


def main():
    N, K, Q = map(int, input().split())

    A1, A2 = [0 for _ in range(K)], [0 for _ in range(N - K)]
    heapq.heapify(A1)
    heapq.heapify(A2)
    ans = 0
    num = [0 for _ in range(N)]
    for _ in range(Q):
        x, y = map(int, input().split())

        heapq.heappush(A2, -y)
        pre = num[x - 1]
        num[x - 1] = y

        try:
            i = A1.index(pre)
            ans -= A1[i]
            del A1[i]
        except ValueError:
            try:
                i = A2.index(-pre)
                del A2[i]
            except ValueError:
                pass

        while len(A1) < K:
            a = -heapq.heappop(A2)
            heapq.heappush(A1, a)
            ans += a

        while A1[0] < -A2[0]:
            a1 = heapq.heappop(A1)
            a2 = -heapq.heappop(A2)

            heapq.heappush(A1, a2)
            heapq.heappush(A2, -a1)

            ans += a2 - a1

        print(ans)


if __name__ == "__main__":
    main()
