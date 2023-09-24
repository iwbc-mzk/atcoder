import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    MAX = 10**6 + 1

    ok = [True for _ in range(MAX)]
    cnt = [0 for _ in range(MAX)]
    for a in A:
        cnt[a] += 1
        if cnt[a] > 1:
            ok[a] = False
            continue

        for ai in range(a * 2, MAX, a):
            ok[ai] = False

    ans = 0
    for a in A:
        if ok[a]:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
