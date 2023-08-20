import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l = []
    ans = 0
    for a in A:
        if len(l) == 0 or l[-1][0] != a:
            l.append([a, 1])
            ans += 1
        else:
            l[-1][1] += 1
            ans += 1
            if l[-1][1] == l[-1][0]:
                ans -= l.pop()[1]

        print(ans)


if __name__ == "__main__":
    main()
