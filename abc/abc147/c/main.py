import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())

    XY = []
    for _ in range(N):
        A = int(input())
        xy = []
        for _ in range(A):
            x, y = map(int, input().split())
            xy.append((x, y))
        XY.append(xy)

    ans = 0
    for i in range(2**N):
        correct_flg = True
        for j, xy in enumerate(XY):
            if not (i >> j & 1):
                continue

            for x, y in xy:
                v = y == 1
                if v != bool((i >> (x - 1) & 1)):
                    correct_flg = False
                    break

            if not correct_flg:
                break

        if correct_flg:
            ans = max(ans, i.bit_count())

    print(ans)


if __name__ == "__main__":
    main()
