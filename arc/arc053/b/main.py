import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    S = input()

    C = defaultdict(int)
    for s in S:
        C[s] += 1

    single = 0
    pair = 0
    for v in C.values():
        if v % 2:
            single += 1
        pair += v // 2

    if single and pair:
        ans = 1 + 2 * (pair // single)
    elif single == 0 and pair:
        ans = 2 * pair
    elif single and pair == 0:
        ans = 1
    else:
        ans = 0
    print(ans)


if __name__ == "__main__":
    main()
