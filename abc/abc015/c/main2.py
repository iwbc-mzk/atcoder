import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    T = [list(map(int, input().split())) for _ in range(N)]

    def has_bug(i, t=None):
        bug = False
        for j in range(K):
            if t:
                tt = t ^ T[i][j]
            else:
                tt = T[i][j]

            if i + 1 < N:
                bug |= has_bug(i + 1, tt)
            else:
                if tt == 0:
                    bug = True
                else:
                    bug |= False

            if bug:
                pass
        return bug

    print("Found" if has_bug(0) else "Nothing")


if __name__ == "__main__":
    main()
