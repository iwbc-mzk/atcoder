import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    ans = [i for i in range(1, N + 1)]
    ans[-1], ans[-2] = ans[-2], ans[-1]
    for n in range(N, 0, -2):
        for i in range(n - 1):
            ans.append(n)
            if i != n - 2:
                ans.append(n - 1)

    print(*ans)


if __name__ == "__main__":
    main()
