import sys

sys.setrecursionlimit(10**9)


def main():
    M = int(input())
    D = list(map(int, input().split()))

    days = sum(D)
    middle = (days + 1) // 2

    s = 0
    for i in range(1, M + 1):
        if s + D[i - 1] < middle:
            s += D[i - 1]
        else:
            print(i, middle - s)
            break


if __name__ == "__main__":
    main()
