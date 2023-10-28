import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    for i in range(N, N * 10**2):
        n = str(i)
        if int(n[0]) * int(n[1]) == int(n[2]):
            print(n)
            return


if __name__ == "__main__":
    main()
