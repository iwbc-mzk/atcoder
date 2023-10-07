import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()
    flg = True
    for i in range(1, 17, 2):
        if S[i] != "0":
            flg = False
            break

    print("Yes" if flg else "No")


if __name__ == "__main__":
    main()
