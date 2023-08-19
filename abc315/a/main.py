import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()
    d = ["a", "e", "i", "o", "u"]
    s = ""
    for si in S:
        if si in d:
            continue
        else:
            s += si

    print(s)


if __name__ == "__main__":
    main()
