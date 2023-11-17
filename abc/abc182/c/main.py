import sys
from itertools import combinations

sys.setrecursionlimit(10**9)


def main():
    N = list(map(int, list(input())))

    s = sum(N)
    for n in range(len(N)):
        for comb in combinations(range(len(N)), n):
            v = s
            for i in comb:
                v -= N[i]

            if v and v % 3 == 0:
                print(n)
                return

    print(-1)


if __name__ == "__main__":
    main()
