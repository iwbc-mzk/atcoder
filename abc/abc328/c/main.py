import sys

sys.setrecursionlimit(10**9)


def main():
    N, Q = map(int, input().split())
    S = input()

    C = [0]
    for i in range(N - 1):
        C.append(C[-1])
        if S[i] == S[i + 1]:
            C[-1] += 1

    for _ in range(Q):
        l, r = map(int, input().split())
        ans = C[r - 1] - C[l - 1]
        print(ans)


if __name__ == "__main__":
    main()
