import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    SA = deque(list(input().upper()))
    SB = deque(list(input().upper()))
    SC = deque(list(input().upper()))

    S = {"A": SA, "B": SB, "C": SC}

    def rec(l: deque, abc):
        if not l:
            print(abc)
            return

        v = l.popleft()

        return rec(S[v], v)

    rec(S["A"], "A")


if __name__ == "__main__":
    main()
