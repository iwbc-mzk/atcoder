from collections import defaultdict


def main():
    N = int(input())
    S = input()
    W = list(map(int, input().split()))

    w = defaultdict(int)
    for i, wi in enumerate(W):
        w[wi] += 1 if S[i] == "0" else -1

    cnt = S.count("1")
    ans = cnt
    W = list(set(W))
    W.sort()
    for wi in W:
        cnt += w[wi]
        ans = max(ans, cnt)

    print(ans)


if __name__ == "__main__":
    main()
