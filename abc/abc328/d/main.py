import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    ans = []
    for s in S:
        ans.append(s)
        if ans[-3:] == ["A", "B", "C"]:
            for _ in range(3):
                ans.pop()

    print("".join(ans))


if __name__ == "__main__":
    main()
