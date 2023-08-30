import sys

sys.setrecursionlimit(10**9)


def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())

        k = 0
        while N >= 3:
            k += N % 3
            N //= 3
        else:
            k += N

        if k > K:
            print("No")
        elif (K - k) % 2 == 0:
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()
