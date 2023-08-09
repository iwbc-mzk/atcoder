import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    N, X = map(int, input().split())
    S = input()

    q = deque()
    for i in range(len(S)):
        if i == 0:
            q.append(S[i])
        else:
            if q:
                r = q.pop()
                if S[i] == "U" and r in ("L", "R"):
                    continue
                else:
                    q.append(r)
                    q.append(S[i])
            else:
                q.append(S[i])

    ans = X
    while q:
        si = q.popleft()
        if si == "U":
            ans //= 2
        elif si == "L":
            ans *= 2
        else:
            ans = ans * 2 + 1

    print(ans)


if __name__ == "__main__":
    main()
