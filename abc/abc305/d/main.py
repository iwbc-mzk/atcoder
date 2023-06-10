import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    T = {}
    T[0] = 0
    for i in range(1, N):
        a, b = A[i], A[i - 1]
        if i % 2:
            T[a] = T[b]
        else:
            T[a] = T[b] + A[i] - A[i - 1]

    for _ in range(Q):
        l, r = map(int, input().split())
        li = bisect.bisect_left(A, l)
        ri = bisect.bisect_left(A, r)
        s = T[A[ri]] - T[A[li]]
        if li % 2 == 0:
            s += A[li] - l
        if ri % 2 == 0:
            s -= A[ri] - r
        print(s)


if __name__ == "__main__":
    main()
