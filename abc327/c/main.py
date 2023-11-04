import sys

sys.setrecursionlimit(10**9)


def main():
    A = [list(map(int, input().split())) for _ in range(9)]

    for r in range(9):
        flg = [False for _ in range(9)]
        for c in range(9):
            a = A[r][c]
            if not flg[a - 1]:
                flg[a - 1] = True
            else:
                print("No")
                return

    for c in range(9):
        flg = [False for _ in range(9)]
        for r in range(9):
            a = A[r][c]
            if not flg[a - 1]:
                flg[a - 1] = True
            else:
                print("No")
                return

    for r, c in [
        (1, 1),
        (1, 4),
        (1, 7),
        (4, 1),
        (4, 4),
        (4, 7),
        (7, 1),
        (7, 4),
        (7, 7),
    ]:
        flg = [False for _ in range(9)]
        flg[A[r][c] - 1] = True
        for dr, dc in [
            (1, 0),
            (1, 1),
            (0, 1),
            (-1, 1),
            (-1, 0),
            (-1, -1),
            (0, -1),
            (1, -1),
        ]:
            a = A[r - dr][c - dc]
            if not flg[a - 1]:
                flg[a - 1] = True
            else:
                print("No")
                return

    print("Yes")


if __name__ == "__main__":
    main()
