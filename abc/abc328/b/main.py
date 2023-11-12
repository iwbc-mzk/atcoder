import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    D = list(map(int, input().split()))

    ans = 0
    for i in range(1, N + 1):
        for d in range(1, D[i - 1] + 1):
            si = set(list(str(i)))
            sd = set(list(str(d)))
            si.update(sd)
            if len(si) == 1:
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
