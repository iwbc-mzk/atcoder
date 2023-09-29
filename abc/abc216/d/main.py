import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    K = []
    A = []
    for _ in range(M):
        k = int(input())
        K.append(k)
        a = deque(map(int, input().split()))
        A.append(a)

    D = defaultdict(list)

    def rec(i):
        if len(A[i]) == 0:
            return

        v = A[i].popleft()
        D[v].append(i)
        if len(D[v]) == 2:
            for j in D[v]:
                rec(j)

    for i in range(M):
        rec(i)

    result = True
    for a in A:
        if a:
            result = False
            break

    print("Yes" if result else "No")


if __name__ == "__main__":
    main()
