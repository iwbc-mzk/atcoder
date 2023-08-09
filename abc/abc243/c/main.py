import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]
    S = input()

    D = defaultdict(list)
    for i, (x, y) in enumerate(XY):
        D[y].append((x, 1) if S[i] == "R" else (x, -1))

    ans = False
    for s in D.values():
        t = False
        for x, v in sorted(s):
            if v > 0:
                t = True
            else:
                if t:
                    ans = True
                    break

    print("Yes" if ans else "No")


if __name__ == "__main__":
    main()
