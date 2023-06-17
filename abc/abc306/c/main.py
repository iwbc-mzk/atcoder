from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    cnt = defaultdict(int)
    ans = [-1 for _ in range(3 * N)]
    for i, a in enumerate(A):
        cnt[a] += 1
        if cnt[a] == 2:
            ans[i] = a

    ans = [n for n in ans if n != -1]
    print(*ans)


if __name__ == "__main__":
    main()
