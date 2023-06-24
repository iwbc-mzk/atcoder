from collections import deque


def main():
    N = int(input())
    S = input()

    I = set(range(len(S)))

    l = deque()
    e = set()
    for i, si in enumerate(S):
        if si == "(":
            l.append(i)

        if si == ")":
            if l:
                e.union(set(range(l.pop(), i + 1)))

    s = "".join(S[i] for i in range(N) if i not in e)
    print(s)


if __name__ == "__main__":
    main()
