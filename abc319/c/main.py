from itertools import permutations


def main():
    C = [list(map(int, input().split())) for _ in range(3)]
    D = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

    perms = permutations(D, 9)

    total = 1
    for i in range(1, 10):
        total *= i

    ok = 0
    for perm in perms:
        m = [[False for _ in range(3)] for _ in range(3)]
        flg = True

        for p in perm:
            r, c = p

            pre_r = None
            for ci in range(3):
                if m[r][ci]:
                    if not pre_r:
                        pre_r = C[r][ci]
                    else:
                        if pre_r == C[r][ci]:
                            flg = False
                            break

            pre_c = None
            for ri in range(3):
                if m[ri][c]:
                    if not pre_c:
                        pre_c = C[ri][c]
                    else:
                        if pre_c == C[ri][c]:
                            flg = False
                            break

            if r == c:
                pre = None
                for i in range(3):
                    if m[i][i]:
                        if not pre:
                            pre = C[i][i]
                        else:
                            if pre == C[i][i]:
                                flg = False
                                break

                if r == 1 and c == 1:
                    pre = None
                    for i, j in [(0, 2), (1, 1), (2, 0)]:
                        if m[i][j]:
                            if not pre:
                                pre = C[i][j]
                            else:
                                if pre == C[i][j]:
                                    flg = False
                                    break
            elif (r == 2 and c == 0) or (r == 0 and c == 2):
                pre = None
                for i, j in ((0, 2), (1, 1), (2, 0)):
                    if m[i][j]:
                        if not pre:
                            pre = C[i][j]
                        else:
                            if pre == C[i][j]:
                                flg = False
                                break

            m[r][c] = True
            if not flg:
                break

        if flg:
            ok += 1

    print(ok / total)


if __name__ == "__main__":
    main()
