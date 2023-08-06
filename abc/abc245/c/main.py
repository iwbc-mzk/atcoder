import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    S = set()
    for i in range(N):
        s = set()
        if i == 0:
            s.add(A[i])
            s.add(B[i])
        else:
            for v in S:
                if abs(v - A[i]) <= K:
                    s.add(A[i])
                if abs(v - B[i]) <= K:
                    s.add(B[i])

        if len(s) == 0:
            print("No")
            return
        else:
            S = s

    print("Yes")


if __name__ == "__main__":
    main()
