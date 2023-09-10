import sys

sys.setrecursionlimit(10**9)


def main():
    S = input()
    T = input()

    # アルファベット毎の変換表
    F = [[0 for _ in range(26)] for _ in range(26)]

    for s, t in zip(S, T):
        F[ord(s) - ord("a")][ord(t) - ord("a")] += 1

    # 異なるアルファベットが同じアルファベットに変換されるようなことはできない
    for i in range(26):
        c = 0
        for j in range(26):
            if F[i][j]:
                c += 1
        if c > 1:
            print("No")
            return

    for j in range(26):
        c = 0
        for i in range(26):
            if F[i][j]:
                c += 1
        if c > 1:
            print("No")
            return

    print("Yes")


if __name__ == "__main__":
    main()
