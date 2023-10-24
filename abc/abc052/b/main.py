import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    S = input()

    x = 0
    ans = 0
    for s in S:
        if s == "I":
            x += 1
        else:
            x -= 1

        ans = max(ans, x)

    print(ans)


if __name__ == "__main__":
    main()
