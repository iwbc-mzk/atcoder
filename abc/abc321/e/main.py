import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    T = int(input())

    for _ in range(T):
        N, X, K = map(int, input().split())

        q = deque()
        q.append((X, 0))
        ans = set()
        visited = set()
        while q:
            x, d = q.popleft()
            if d == K:
                ans.add(x)
                continue

            if x * 2 <= N and x * 2 not in visited:
                q.append((x * 2, d + 1))
                visited.add(x * 2)
            if x * 2 + 1 <= N and (x * 2 + 1) not in visited:
                q.append((x * 2 + 1, d + 1))
                visited.add(x * 2 + 1)
            if x != 1 and (x // 2) not in visited:
                q.append((x // 2, d + 1))
                visited.add(x // 2)

        print(len(ans))


if __name__ == "__main__":
    main()
