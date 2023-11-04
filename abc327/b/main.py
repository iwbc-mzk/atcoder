import sys

sys.setrecursionlimit(10**9)


def main():
    B = int(input())

    for a in range(1, 20):
        if a**a == B:
            print(a)
            return
    else:
        print(-1)


if __name__ == "__main__":
    main()
