import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


def cost(c1, c2, A, C):
    cost = 0
    for i, a in enumerate(A):
        if i % 2 == 0 and a != c1:
            cost += C
        elif i % 2 and a != c2:
            cost += C

    return cost


def main():
    N, C = map(int, input().split())
    A = [int(input()) for _ in range(N)]

    combs = combinations(range(1, 11), 2)
    ans = float("inf")
    for c1, c2 in combs:
        ans = min(ans, cost(c1, c2, A, C))
        ans = min(ans, cost(c2, c1, A, C))

    print(ans)


if __name__ == "__main__":
    main()
