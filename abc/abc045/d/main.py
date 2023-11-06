import sys
from collections import defaultdict
from itertools import product

sys.setrecursionlimit(10**9)


def main():
    H, W, N = map(int, input().split())

    C = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        for da, db in product((0, 1, -1), (0, 1, -1)):
            aa, bb = a + da, b + db
            if not (1 <= aa <= H - 2) or not (1 <= bb <= W - 2):
                continue

            C[(aa, bb)] += 1

    ans = [0] * 10
    ans[0] = (H - 2) * (W - 2)
    for v in C.values():
        if v:
            ans[v] += 1
            ans[0] -= 1

    for a in ans:
        print(a)


if __name__ == "__main__":
    main()
