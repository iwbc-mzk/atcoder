import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans, ans_c = 0, 0
    for k in range(2, max(A) + 1):
        c = 0
        for a in A:
            if a % k == 0:
                c += 1

        if c > ans_c:
            ans_c = c
            ans = k

    print(ans)


if __name__ == "__main__":
    main()
