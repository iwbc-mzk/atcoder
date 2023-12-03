import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    C = defaultdict(int)
    pre = ""
    c = 0
    for i in range(N):
        if S[i] != pre:
            if c:
                C[pre] = max(C[pre], c)
            pre = S[i]
            c = 1
        else:
            c += 1
    else:
        if c:
            C[pre] = max(C[pre], c)

    ans = 0
    for c, v in C.items():
        ans += v

    print(ans)


if __name__ == "__main__":
    main()
