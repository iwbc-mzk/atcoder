import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    W = [[0, i + 1] for i in range(N)]
    for i, s in enumerate(S):
        for si in s:
            if si == "o":
                W[i][0] += 1

    W.sort(lambda x: (-x[0], x[1]))
    ans = []
    for w in W:
        ans.append(w[1])

    print(*ans)


if __name__ == "__main__":
    main()
