from random import randint
from time import perf_counter


def mex(i, j, k):
    for n in range(3):
        if n not in (i, j, k):
            return n
    else:
        return 3


def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = input()

    SA = []
    for s, a in zip(S, A):
        SA.append(s + str(a))

    T = set([""])
    for m in ["M0", "M1", "M2"]:
        T.add(m)
        for e in ["E0", "E1", "E2"]:
            T.add(m + e)

    DPM = [0, 0, 0]
    DPE = [[0, 0, 0] for _ in range(3)]
    ans = 0
    for i in range(N):
        s, a = S[i], A[i]
        if s == "M":
            DPM[a] += 1
        elif s == "E":
            for j in range(3):
                DPE[j][a] += DPM[j]
        elif s == "X":
            for k in range(3):
                for l in range(3):
                    ans += DPE[k][l] * mex(k, l, a)

    print(ans)


if __name__ == "__main__":
    main()
