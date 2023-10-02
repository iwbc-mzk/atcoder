import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    if N % 2:
        print("No")
    else:
        print("Yes" if S[: N // 2] == S[N // 2 :] else "No")


if __name__ == "__main__":
    main()
