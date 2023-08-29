import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0] * (N // 2) + A[N // 2 :]

    for n in range(N // 2, 0, -1):
        i = 2
        t = 0
        while n * i <= N:
            t += B[n * i - 1]
            i += 1

        if t % 2 == A[n - 1]:
            B[n - 1] = 0
        else:
            B[n - 1] = 1

    M = sum(B)
    print(M)
    if M:
        print(*[i for i, v in enumerate(B, 1) if v])


if __name__ == "__main__":
    main()
