import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    W = input().split()

    M = {
        "b": "1",
        "c": "1",
        "d": "2",
        "w": "2",
        "t": "3",
        "j": "3",
        "f": "4",
        "q": "4",
        "l": "5",
        "v": "5",
        "s": "6",
        "x": "6",
        "p": "7",
        "m": "7",
        "h": "8",
        "k": "8",
        "n": "9",
        "g": "9",
        "z": "0",
        "r": "0",
    }

    ans = []
    for w in W:
        n = []
        for wi in w:
            wi = wi.lower()
            if wi in M:
                n.append(M[wi])

        if n:
            n = "".join(n)
            ans.append(n)

    print(*ans)


if __name__ == "__main__":
    main()
