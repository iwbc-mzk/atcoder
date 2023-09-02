import sys

sys.setrecursionlimit(10**9)


def main():
    N, D, P = map(int, input().split())
    F = list(map(int, input().split()))

    F.sort(reverse=True)
    k = 0
    c = 0
    while sum(F[k : k + D]) > P:
        k += D
        c += 1

    ans = P * c + sum(F[k:])
    print(ans)


if __name__ == "__main__":
    main()
