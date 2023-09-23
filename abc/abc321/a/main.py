import sys

sys.setrecursionlimit(10**9)


def main():
    N = input()

    pre = None
    for n in N:
        n = int(n)
        if pre is None:
            pre = n
        else:
            if pre <= n:
                print("No")
                break
            pre = n
    else:
        print("Yes")


if __name__ == "__main__":
    main()
