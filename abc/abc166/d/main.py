import sys

sys.setrecursionlimit(10**9)


def main():
    X = int(input())

    for a in range(-(10**3), 10**3):
        for b in range(-(10**3), 10**3):
            if a**5 - b**5 == X:
                print(a, b)
                return


if __name__ == "__main__":
    main()
