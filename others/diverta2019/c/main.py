import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = [input() for _ in range(N)]

    RA, LB, AB, NN = [], [], [], []

    ans = 0
    for s in S:
        ans += s.count("AB")
        if s.endswith("A") and s.startswith("B"):
            AB.append(s)
        elif s.endswith("A"):
            RA.append(s)
        elif s.startswith("B"):
            LB.append(s)
        else:
            NN.append(s)

    a, b, ab = len(RA), len(LB), len(AB)
    if ab == 0:
        ans += min(a, b)
    else:
        if a or b:
            ans += min(a, b) + ab
        else:
            ans += ab - 1

    print(ans)


if __name__ == "__main__":
    main()
