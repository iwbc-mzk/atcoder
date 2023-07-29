import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()

    L = ["ACE", "BDF", "CEG", "DFA", "EGB", "FAC", "GBD"]
    if S in L:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
