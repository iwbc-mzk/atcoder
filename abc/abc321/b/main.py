import sys

sys.setrecursionlimit(10**9)


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    s = sum(A[1:-1])
    for i in range(101):
        s = sum(A[1:-1])
        if i < A[0]:
            s += A[0]
        elif A[0] <= i <= A[-1]:
            s += i
        else:
            s += A[-1]

        if s >= X:
            print(i)
            return
    else:
        print(-1)


if __name__ == "__main__":
    main()
