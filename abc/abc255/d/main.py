import bisect


def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    AA = [0 for _ in range(N + 1)]
    for i in range(N):
        AA[i + 1] += AA[i] + A[i]

    for _ in range(Q):
        X = int(input())
        i = bisect.bisect_left(A, X)

        left_sum = AA[i]
        left_num = i

        right_sum = AA[-1] - left_sum
        right_num = N - left_num

        ans = X * left_num - left_sum + right_sum - X * right_num
        print(ans)


if __name__ == "__main__":
    main()
