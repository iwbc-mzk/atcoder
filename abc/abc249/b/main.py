from collections import defaultdict


def main():
    S = input()

    l = False
    s = False
    d = True
    D = defaultdict(int)
    for si in S:
        if si.islower():
            s = True

        if si.isupper():
            l = True

        D[si] += 1
        if D[si] > 1:
            d = False

    if l and s and d:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
