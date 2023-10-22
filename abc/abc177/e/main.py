import sys
from math import gcd

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    if gcd(*A) != 1:
        print("not coprime")
    else:
        l = set(A)
        max_a = max(A)
        for t in range(2, max_a + 1):
            i = 1
            c = 0
            while t * i <= max_a:
                if t * i in l:
                    c += 1
                i += 1

            if c >= 2:
                print("setwise coprime")
                return
        else:
            print("pairwise coprime")


if __name__ == "__main__":
    main()
