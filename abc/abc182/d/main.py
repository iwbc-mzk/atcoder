import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    AA = [0]
    for a in A:
        AA.append(AA[-1] + a)

    ma = [0]
    for a in AA:
        ma.append(max(ma[-1], a))

    ans = 0
    pre = 0
    for n in range(N):
        ans = max(ans, pre + ma[n])
        pre = pre + AA[n] + A[n]

    print(max(ans, pre))


if __name__ == "__main__":
    main()
