import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    C, S, F = [], [], []
    for _ in range(N - 1):
        c, s, f = map(int, input().split())
        C.append(c)
        S.append(s)
        F.append(f)

    for start in range(N):
        time = 0
        for i in range(start, N - 1):
            if time < S[i]:
                time = S[i]
            else:
                if time % F[i]:
                    time += F[i] - time % F[i]

            time += C[i]

        print(time)


if __name__ == "__main__":
    main()
