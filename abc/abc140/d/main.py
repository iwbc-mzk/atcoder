import sys

sys.setrecursionlimit(10**9)

from typing import Iterable


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
    N, K = map(int, input().split())
    S = input()

    s = run_length_encoding(S)

    ss = len(s)
    for _ in range(K):
        if ss >= 3:
            ss -= 2
        elif ss == 2:
            ss = 1

    print(N - ss)


if __name__ == "__main__":
    main()
