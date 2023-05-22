import bisect


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    K = [int(input()) for _ in range(Q)]

    memo = []
    cnt = 0
    last = 0
    for a in A:
        cnt += a - last - 1
        memo.append(cnt)
        last = a

    for k in K:
        idx = bisect.bisect_right(memo, k)

        if memo[idx - 1] == k:
            i = bisect.bisect_left(memo, k)
            ans = A[i] - 1
        elif idx == len(memo):
            ans = A[-1] + (k - memo[-1])
        elif idx == 0:
            ans = k
        else:
            ans = A[idx - 1] + (k - memo[idx - 1])

        print(ans)


if __name__ == "__main__":
    main()
