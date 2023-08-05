import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    s = sum(A)

    B = [s // N] * N
    for i in range(s % N):
        B[-1 - i] += 1

    ans = 0
    for a, b in zip(A, B):
        ans += abs(a - b)

    print(ans // 2)


if __name__ == "__main__":
    main()
