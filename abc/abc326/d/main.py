import sys
from itertools import combinations, product, permutations

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    R = list(input())
    C = list(input())

    for combs in product(combinations(range(5), 3), repeat=N):
        A = [["." for _ in range(N)] for _ in range(N)]
        ok = True
        for i, comb in enumerate(combs):
            for c in comb:
                A[i][c] = "ABC"[c]

            if A[i][min(comb)] != R[i]:
                ok = False
                break
        
        if not ok:
            continue

        AA = ["AC..B" ".BA.C" "C.BA." "BA.C." "..CBA"]
        for i, a in enumerate(A):
            if AA[i] != "".join(a):
                break
        else:
            pass

        for c in range(N):
            abc = set()
            seen = False
            for r in range(N):
                if A[r][c] == ".":
                    continue

                if A[r][c] in abc:
                    ok = False
                    break
                else:
                    abc.add(A[r][c])

                if not seen:
                    if A[r][c] != C[c]:
                        ok = False
                        break
                    seen = True

        if ok:
            print("Yes")
            for a in A:
                print("".join(a))

    print("No")


if __name__ == "__main__":
    main()
