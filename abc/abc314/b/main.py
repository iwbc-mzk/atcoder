import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    d = defaultdict(list)
    for i in range(1, N + 1):
        C = int(input())
        A = list(map(int, input().split()))

        for a in A:
            d[a].append((C, i))

    X = int(input())
    l = sorted(d[X])

    ans = []
    t = 0
    for i, li in enumerate(l):
        if i == 0:
            t = li[0]
            ans.append(li[1])
        else:
            if li[0] == t:
                ans.append(li[1])
            else:
                break

    print(len(ans))
    print(*ans)


if __name__ == "__main__":
    main()
