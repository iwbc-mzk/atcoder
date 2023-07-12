import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    if N % 2:
        return

    l = []

    def rec(s, c):
        if len(s) == N:
            if c == 0:
                l.append(s)
            return

        if c == 0:
            s += "("
            rec(s, c + 1)
        else:
            rec(s + "(", c + 1)
            rec(s + ")", c - 1)

    rec("", 0)
    l.sort()
    for li in l:
        print(li)


if __name__ == "__main__":
    main()
