import sys

sys.setrecursionlimit(10**9)

from typing import Iterable
from math import perm


# ランレングス圧縮
def run_length_encoding(s: Iterable):
    pre = s[0]
    cnt = 0
    result = []
    for si in s:
        if si == pre:
            cnt += 1
        else:
            result.append((pre, cnt))
            pre = si
            cnt = 1
    else:
        result.append((pre, cnt))

    return result


def main():
    N = int(input())
    T = list(int(input()) for _ in range(N))
    MOD = 10**9 + 7

    T.sort()
    ans1 = 0
    k = 0
    for t in T:
        k += t
        ans1 += k

    TT = run_length_encoding(T)
    ans2 = 1
    memo = {}
    for _, v in TT:
        if v in memo:
            ans2 *= memo[v]
        else:
            memo[v] = perm(v, v)
            ans2 *= memo[v]
        ans2 %= MOD

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
