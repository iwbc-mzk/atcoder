import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    D = defaultdict(list)
    for _ in range(N):
        f, s = map(int, input().split())
        D[f].append(s)

    diff_list = []
    same = 0
    for k in D:
        D[k].sort(reverse=True)
        diff_list.append(D[k][0])
        if len(D[k]) >= 2:
            same = max(same, D[k][0] + D[k][1] // 2)

    diff_list.sort(reverse=True)
    if len(diff_list) >= 2:
        diff = diff_list[0] + diff_list[1]
    else:
        diff = 0

    print(max(same, diff))


if __name__ == "__main__":
    main()
