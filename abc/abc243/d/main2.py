import sys

sys.setrecursionlimit(10**9)


def main():
    N, X = map(int, input().split())
    S = input()

    ans = list(bin(X))
    for s in S:
        if s == "U":
            ans.pop()
        elif s == "L":
            ans.append("0")
        else:
            ans.append("1")

    ans = "".join(ans)

    print(int(ans, 2))


if __name__ == "__main__":
    main()
