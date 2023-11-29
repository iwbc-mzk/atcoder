import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    for i, si in enumerate(S):
        if si == "A":
            l = i
            break

    for j, sj in enumerate(reversed(S)):
        if sj == "Z":
            r = len(S) - 1 - j
            break

    print(r - l + 1)


if __name__ == "__main__":
    main()
