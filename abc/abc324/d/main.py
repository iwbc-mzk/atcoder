import sys
from collections import defaultdict
import math

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    C = [0 for _ in range(11)]
    for s in S:
        C[int(s)] += 1

    ans = []
    max_S = int("".join(sorted(S, reverse=True)))
    for v in range(math.ceil(math.sqrt(max_S)) + 1):
        vv = str(v**2)
        CV = [0 for _ in range(11)]
        for vi in vv:
            CV[int(vi)] += 1

        for i in range(10):
            if C[i] != CV[i] and i != 0:
                break
        else:
            ans.append(v)

    print(len(ans))


if __name__ == "__main__":
    main()
