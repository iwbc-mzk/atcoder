import sys
from itertools import combinations, product, permutations

sys.setrecursionlimit(10**9)


def head_check(L: list[list], S: str):
    h = []
    for i in range(len(L)):
        for j in range(len(L)):
            if L[i][j] != ".":
                h.append(L[i][j])
                break

    return S == "".join(h)


def main():
    N = int(input())
    R = input()
    C = input()

    for a, b, c in product(permutations(range(N)), repeat=3):
        if any(ai == bi or bi == ci or ci == ai for ai, bi, ci in zip(a, b, c)):
            continue

        A = [["." for _ in range(N)] for _ in range(N)]

        for i, ai in enumerate(a):
            A[i][ai] = "A"

        for i, bi in enumerate(b):
            A[i][bi] = "B"

        for i, ci in enumerate(c):
            A[i][ci] = "C"

        AA = list(zip(*A))  # 行列入れ替え
        if head_check(A, R) and head_check(AA, C):
            print("Yes")
            for a in A:
                print("".join(a))
            return

    print("No")


if __name__ == "__main__":
    main()
