import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    AA = [0]
    t = 0
    for a in A:
        t += a
        t %= 360
        AA.append(t)

    AA.sort()
    ans = 0
    for i in range(1, N):
        ans = max(ans, AA[i] - AA[i - 1])
    else:
        ans = max(ans, 360 - AA[-1])

    print(ans)


if __name__ == "__main__":
    main()
