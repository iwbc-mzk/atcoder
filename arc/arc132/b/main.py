from math import inf
from collections import deque


def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = inf
    for s, e in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        cnt = 0
        p = deque(P)
        if s:
            p.reverse()
            cnt += 1

        if e:
            while p[0] != N:
                v = p.popleft()
                p.append(v)
                cnt += 1

            p.reverse()
            cnt += 1
        else:
            while p[0] != 1:
                v = p.popleft()
                p.append(v)
                cnt += 1

        for i in range(N - 1):
            if p[i] > p[i + 1]:
                break
        else:
            ans = min(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
