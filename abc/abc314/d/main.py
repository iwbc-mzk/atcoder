import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = list(input())
    Q = int(input())

    ul = 0
    s = set()
    for _ in range(Q):
        t, x, c = input().split()
        t, x = int(t), int(x)
        if t == 1:
            S[x - 1] = c
            s.add(x)
        elif t == 2:
            ul = -1
            s = set()
        else:
            ul = 1
            s = set()

    if ul == 0:
        print("".join(S))
    else:
        ans = []
        for i, si in enumerate(S, 1):
            if i in s:
                ans.append(si)
            else:
                ans.append(si.upper() if ul == 1 else si.lower())

        print("".join(ans))


if __name__ == "__main__":
    main()
