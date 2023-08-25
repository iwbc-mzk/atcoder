import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()
    l, r = 0, len(S) - 1
    edge = True
    while r >= l:
        if S[l] != S[r]:
            if edge and S[r] == "a":
                r -= 1
            else:
                print("No")
                return
        else:
            if edge and S[l] != "a":
                edge = False
            l += 1
            r -= 1

    print("Yes")


if __name__ == "__main__":
    main()
