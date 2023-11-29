import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    r = 0
    for i in range(N - 1):
        if A[i] == A[i + 1]:
            r += 1

    print(N - (r - r % 2) - 2 * (r % 2))


if __name__ == "__main__":
    main()
