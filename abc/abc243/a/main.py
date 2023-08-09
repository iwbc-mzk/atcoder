import sys

sys.setrecursionlimit(10**9)


def main():
    V, A, B, C = map(int, input().split())

    ANS = ["F", "M", "T"]
    D = [A, B, C]
    i = 0
    while V >= 0:
        d = D[i % 3]
        if V < d:
            print(ANS[i % 3])
            return

        V -= d
        i += 1


if __name__ == "__main__":
    main()
