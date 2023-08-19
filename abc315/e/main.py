import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    C = []
    P = []
    for _ in range(N):
        c, *p = map(int, input().split())
        C.append(c)
        P.append(p)

    q = deque()
    for p in P[0]:
        q.append(p)
    read = set()
    ans = []
    while q:
        if q[0] not in read:
            if C[q[0] - 1] == 0:
                read.add(q[0])
                ans.append(q[0])
                q.popleft()
            else:
                read_flg = True
                for p in P[q[0] - 1]:
                    if p not in read:
                        q.appendleft(p)
                        read_flg = False
                if read_flg:
                    read.add(q[0])
                    ans.append(q[0])
                    q.popleft()

        else:
            q.popleft()

    print(*ans)


if __name__ == "__main__":
    main()
