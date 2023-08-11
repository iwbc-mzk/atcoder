import sys

sys.setrecursionlimit(10**9)


def convert(s, l):
    return chr(ord("A") + ((ord(s) - ord("A")) + l) % 3)


def rec(S, t, k):
    if t == 0:
        return S[k]
    if k == 0:
        return convert(S[0], t)

    return convert(rec(S, t - 1, k // 2), k % 2 + 1)


def main():
    S = input()
    Q = int(input())
    for _ in range(Q):
        t, k = map(int, input().split())
        a = rec(S, t, k - 1)

        print(a)


if __name__ == "__main__":
    main()
