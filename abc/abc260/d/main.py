import bisect
from collections import defaultdict


def main():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))

    table = []
    cnt = defaultdict(set)
    ans = [-1 for _ in range(N)]
    for turn, p in enumerate(P, 1):
        idx = bisect.bisect_left(table, p)
        if idx == len(table):
            table.append(p)
            cnt[p].add(p)
        else:
            cnt[p] = cnt[table[idx]]
            cnt[p].add(p)
            table[idx] = p

        if len(cnt[p]) == K:
            for i in cnt[p]:
                ans[i - 1] = turn
            del table[idx]

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
