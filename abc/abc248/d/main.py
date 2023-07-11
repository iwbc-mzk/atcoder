from collections import defaultdict
import bisect


def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    D = defaultdict(list)
    for i, a in enumerate(A, 1):
        D[a].append(i)

    for _ in range(Q):
        L, R, X = map(int, input().split())
        l = bisect.bisect_left(D[X], L)
        r = bisect.bisect_right(D[X], R)
        print(r - l)


if __name__ == "__main__":
    main()
