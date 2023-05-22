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
        if memo[-1] < k:
            print(A[-1] + (k - memo[-1]))
        else:
            i = bisect.bisect_left(memo, k)
            print(A[i] - 1 - (memo[i] - k))


if __name__ == "__main__":
    main()
