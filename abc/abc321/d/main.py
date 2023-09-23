import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    N, M, P = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort()
    B.sort()

    BB = [0]
    for i, b in enumerate(B):
        BB.append(BB[i] + b)

    ans = 0
    for a in A:
        p = P - a
        i = bisect.bisect_left(B, p)
        ans += a * i + BB[i] + P * (M - i)

    print(ans)


if __name__ == "__main__":
    main()
