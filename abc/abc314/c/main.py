import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    S = input()
    C = list(map(int, input().split()))

    T = [-1] * (M + 1)
    D = defaultdict(list)
    for c, s in zip(C, S):
        D[c].append(s)

    ans = []
    for c in C:
        ans.append(D[c][T[c] % len(D[c])])
        T[c] += 1

    print("".join(ans))


if __name__ == "__main__":
    main()
