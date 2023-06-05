import bisect
from collections import defaultdict


def main():
    W, H = map(int, input().split())
    N = int(input())
    pq = [tuple(map(int, input().split())) for _ in range(N)]

    A = int(input())
    a = list(map(int, input().split()))
    a.sort()

    B = int(input())
    b = list(map(int, input().split()))
    b.sort()

    n_strawberry = defaultdict(int)
    for p, q in pq:
        x = bisect.bisect_left(a, p)
        y = bisect.bisect_left(b, q)
        n_strawberry[(x, y)] += 1

    n_peices = (A + 1) * (B + 1)
    if len(n_strawberry) != n_peices:
        print(0, max(n_strawberry.values()))
    else:
        print(min(n_strawberry.values()), max(n_strawberry.values()))


if __name__ == "__main__":
    main()
