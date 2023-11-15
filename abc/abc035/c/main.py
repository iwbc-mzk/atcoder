import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())

    C = [0] * (N + 1)
    for _ in range(Q):
        l, r = map(int, input().split())
        C[l - 1] += 1
        C[r] -= 1

    ans = []
    for n in range(N):
        if n != 0:
            C[n] += C[n - 1]

        if C[n] % 2 == 0:
            ans.append("0")
        else:
            ans.append("1")

    print("".join(ans))


if __name__ == "__main__":
    main()
