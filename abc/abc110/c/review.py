from collections import defaultdict


def main():
    S = input()
    T = input()

    ex1 = defaultdict(set)
    ex2 = defaultdict(str)
    for s, t in zip(S, T):
        ex1[t].add(s)
        if s != t:
            if len(ex1[t]) > 1:
                print("No")
                return

            if s in ex2 and ex2[s] != t:
                print("No")
                return

        ex2[s] = t

    print("Yes")


if __name__ == "__main__":
    main()
