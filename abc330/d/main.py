import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    H = [[] for _ in range(N)]
    W = [[] for _ in range(N)]
    for i in range(N):
        S = list(input())
        for j, s in enumerate(S):
            if s == "o":
                H[i].append(j)
                W[j].append(i)

    ans = 0
    for h in range(N):
        for i, hi in enumerate(H[h]):
            hc = len(H[h]) - 1
            wc = len(W[hi]) - 1
            ans += hc * wc

    print(ans)


if __name__ == "__main__":
    main()
