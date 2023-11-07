import sys
from statistics import median

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = [a - i for i, a in enumerate(A, 1)]

    med = median(AA)
    ans = int(sum(abs(a - med) for a in AA))
    print(ans)


if __name__ == "__main__":
    main()
