import heapq


def main():
    N, K = map(int, input().split())
    A, B, C = [], [], []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

        C.append((-b, i))

    heapq.heapify(C)
    ans = 0
    k = 0
    while C and k < K:
        s, i = heapq.heappop(C)
        s = -s
        ans += s
        if i >= 0:
            heapq.heappush(C, (-(A[i] - s), -1))
        k += 1

    print(ans)


if __name__ == "__main__":
    main()
