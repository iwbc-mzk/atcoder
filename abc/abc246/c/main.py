import sys

sys.setrecursionlimit(10**9)


def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)
    for i in range(N):
        a = A[i]
        k = min(K, a // X)
        K -= k
        A[i] -= X * k
        if K == 0:
            break

    if K == 0:
        print(sum(A))
    else:
        if K > N:
            print(0)
        else:
            A.sort(reverse=True)
            print(sum(A[K:]))


if __name__ == "__main__":
    main()
