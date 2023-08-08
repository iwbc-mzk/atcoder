import sys

sys.setrecursionlimit(10**9)


def main():
    S = input().split()
    T = input().split()

    P = []
    for s, t in zip(S, T):
        P.append(0 if s == t else 1)

    print("Yes" if sum(P) in [0, 3] else "No")


if __name__ == "__main__":
    main()
