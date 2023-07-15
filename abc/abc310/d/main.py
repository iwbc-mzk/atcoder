from collections import defaultdict
from math import perm
def main():
    N, T, M = map(int, input().split())

    ans = 0
    t = 1
    for i in range(N):
        if i < T:
            t *= (T - i)
        else:
            t *= T

    ans += t // perm(T, T)

    same = 1
    for i in range(1, N):
        if i < T:
            same *= (T - i)
        else:
            same *= T

    same //= perm(T, T)

    AB = defaultdict(set)
    for _ in range(M):
        A, B = map(int, input().split())
        AB[A].add(B)
        AB[B].add(A)
        ans -= same

    pass


if __name__ == "__main__":
    main()
