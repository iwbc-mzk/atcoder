import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    K = int(input())

    q = deque()
    for i in range(1, 10):
        q.append((1, i))

    ans = list(range(1, 10))
    while q and len(ans) < K:
        i, v = q.popleft()

        vv = v % 10
        for d in [-1, 0, 1]:
            if 0 <= vv + d <= 9:
                nv = 10 * v + (vv + d)
                ans.append(nv)
                q.append((i + 1, nv))

    print(ans[K - 1])


if __name__ == "__main__":
    main()
