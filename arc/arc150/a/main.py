import sys

sys.setrecursionlimit(10**9)


def main():
    T = int(input())

    for _ in range(T):
        N, K = map(int, input().split())
        S = list(input())

        C1 = []
        C0 = []
        c1, c0 = 0, 0
        total_1 = 0
        for i, s in enumerate(S):
            if s == "1":
                c1 += 1
                total_1 += 1
            if s == "0":
                c0 += 1

            if i >= K:
                if S[i - K] == "1":
                    c1 -= 1
                if S[i - K] == "0":
                    c0 -= 1

            if i >= K - 1:
                C1.append(c1)
                C0.append(c0)

        result = 0
        for i in range(N - K + 1):
            if C0[i] == 0 and C1[i] == total_1:
                result += 1

        print("Yes" if result == 1 else "No")


if __name__ == "__main__":
    main()
