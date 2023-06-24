from collections import deque


def main():
    N = int(input())
    S = input()

    A = deque()
    s = []
    for si in S:
        if si == "(":
            s.append(si)
            A.append(len(s) - 1)
        elif si == ")":
            if A:
                a = A.pop()
                del s[a:]
            else:
                s.append(si)
        else:
            s.append(si)

    print("".join(s))


if __name__ == "__main__":
    main()
