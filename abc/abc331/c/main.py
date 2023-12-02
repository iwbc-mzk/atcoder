import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = sorted(A)

    AAA = [0]
    for a in AA:
        AAA.append(AAA[-1] + a)

    ans = []
    for i in range(N):
        a = A[i]
        j = bisect.bisect_right(AA, a)
        ans.append(AAA[-1] - AAA[j])

    print(*ans)


if __name__ == "__main__":
    main()
