import sys
from math import comb

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    ans = 0
    for i in range(1, N):
        ans += N / (N - i)

    print(ans)




if __name__ == "__main__":
    main()
