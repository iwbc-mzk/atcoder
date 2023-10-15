import sys


sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    for i in range(2, 4):
        while N % i == 0:
            N //= i

        if N == 1:
            break

    if N == 1:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
