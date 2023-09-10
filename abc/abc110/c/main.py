import sys

sys.setrecursionlimit(10**9)


# 嘘解法
def main():
    S = input()
    T = input()

    s = [0 for _ in range(26)]
    t = [0 for _ in range(26)]
    for si, ti in zip(S, T):
        s[ord(si) - ord("a")] += 1
        t[ord(ti) - ord("a")] += 1

    s.sort()
    t.sort()

    for si, ti in zip(s, t):
        if si != ti:
            print("No")
            return
    else:
        print("Yes")


if __name__ == "__main__":
    main()
