import sys

sys.setrecursionlimit(10**9)


def main():
    W, H = map(int, input().split())
    if W / H == 4 / 3:
        print("4:3")
    else:
        print("16:9")


if __name__ == "__main__":
    main()
