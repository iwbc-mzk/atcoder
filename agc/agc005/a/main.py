import sys

sys.setrecursionlimit(10**9)


def main():
    X = input()

    T = []
    for x in X:
        T.append(x)
        if T[-2:] == ["S", "T"]:
            for _ in range(2):
                T.pop()
    print(len(T))


if __name__ == "__main__":
    main()
