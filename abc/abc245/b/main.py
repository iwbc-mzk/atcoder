import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = set(map(int, input().split()))
    for i in range(2002):
        if i not in A:
            print(i)
            return


if __name__ == "__main__":
    main()
