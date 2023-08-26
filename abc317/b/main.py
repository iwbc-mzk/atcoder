import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    for i, a in enumerate(A, A[0]):
        if i != a:
            print(i)
            return


if __name__ == "__main__":
    main()
