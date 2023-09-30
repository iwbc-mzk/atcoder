import sys
from itertools import product

sys.setrecursionlimit(10**9)


def main():
    P = []
    p = []
    for i in range(12):
        p.append(list(input()))
        if i % 4 == 3:
            P.append(p.copy())
            p = []

    for dr1, dc1, dr2, dc2, dr3, dc3, r2, r3 in product(
        range(-3, 4),
        range(-3, 4),
        range(-3, 4),
        range(-3, 4),
        range(-3, 4),
        range(-3, 4),
        range(4),
        range(4),
    ):
        if (
            r2 == 3
            and r3 == 0
            and dr1 == -1
            and dc1 == 0
            and dr2 == 1
            and dc2 == -1
            and dr3 == 0
            and dc3 == 1
        ):
            pass

        G = [[0] * 4 for _ in range(4)]
        DRC = [(dr1, dc1), (dr2, dc2), (dr3, dc3)]
        R = [0, r2, r3]
        for i in range(3):
            dr, dc = DRC[i]
            r = R[i]
            flg = True
            for jr in range(4):
                for kc in range(4):
                    if P[i][jr][kc] == ".":
                        continue

                    rjr, rkc = jr, kc
                    for _ in range(r):
                        rjr, rkc = rkc, 3 - rjr

                    rjr, rkc = rjr + dr, rkc + dc

                    if 0 <= rjr < 4 and 0 <= rkc < 4 and G[rjr][rkc] == 0:
                        G[rjr][rkc] = 1
                    else:
                        flg = False
                        break
                if not flg:
                    break
            if not flg:
                break
        else:
            ok = True
            for l in range(4):
                for m in range(4):
                    if G[l][m] != 1:
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                print("Yes")
                return

    print("No")


if __name__ == "__main__":
    main()
