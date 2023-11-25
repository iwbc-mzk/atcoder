import sys
import bisect

sys.setrecursionlimit(10**9)


def main():
    D = int(input())

    memo = []
    for i in range(2 * 10**6 + 1):
        memo.append(i**2)

    ans = float("inf")
    for x in memo:
        r = abs(x - D)
        i = bisect.bisect_left(memo, r)

        v = float("inf")
        if 0 <= i - 1:
            v = min(v, abs(x + memo[i - 1] - D))
        if i < len(memo):
            v = min(v, abs(x + memo[i] - D))
        ans = min(ans, v)

    print(ans)


if __name__ == "__main__":
    main()
