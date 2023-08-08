import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    S = set()
    while True:
        for i in range(1, 2 * N + 2):
            if i in S:
                continue

            S.add(i)
            print(i)
            break

        a = int(input())
        S.add(a)
        if a == 0:
            return


if __name__ == "__main__":
    main()
