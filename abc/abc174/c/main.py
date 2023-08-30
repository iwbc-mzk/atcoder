import sys

sys.setrecursionlimit(10**9)


def main():
    K = int(input())

    a = 0
    for i in range(1, K + 1):
        a *= 10
        a += 7
        a %= K
        if a == 0:
            print(i)
            return
    else:
        print(-1)


if __name__ == "__main__":
    main()
