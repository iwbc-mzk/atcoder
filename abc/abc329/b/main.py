import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = set(map(int, input().split()))
    A = list(A)
    A.sort()
    print(A[-2])


if __name__ == "__main__":
    main()
