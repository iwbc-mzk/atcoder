from collections import deque


def main():
    X, Y, A, B, C = map(int, input().split())
    PA = list(map(int, input().split()))
    QB = list(map(int, input().split()))
    RC = list(map(int, input().split()))

    PA.sort(reverse=True)
    QB.sort(reverse=True)

    a = PA[:X] + QB[:Y] + RC
    a.sort(reverse=True)

    print(sum(a[: X + Y]))


if __name__ == "__main__":
    main()
