import sys

sys.setrecursionlimit(10**9)


def main():
    S = input().split()
    T = input().split()

    M = {t: i for i, t in enumerate(T)}
    S = [M[s] for s in S]

    # 転倒数
    t = 0
    for i in range(3):
        for j in range(i):
            if S[i] < S[j]:
                t += 1

    print("Yes" if t % 2 == 0 else "No")


if __name__ == "__main__":
    main()
