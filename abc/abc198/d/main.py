import sys
from itertools import permutations, combinations

sys.setrecursionlimit(10**9)


def main():
    S1 = input()
    S2 = input()
    S3 = input()

    chars = set()
    for S in [S1, S2, S3]:
        for si in S:
            chars.add(si)

    if len(chars) > 10:
        print("UNSOLVABLE")
        return

    chars = list(chars)
    combs = combinations(range(10), len(chars))
    for comb in combs:
        perms = permutations(comb, len(chars))
        for perm in perms:
            m = {c: perm[i] for i, c in enumerate(chars)}

            if m[S1[0]] == 0 or m[S2[0]] == 0 or m[S3[0]] == 0:
                continue

            s1 = 0
            for i, s in enumerate(S1):
                s1 += m[s] * 10 ** (len(S1) - i - 1)

            s2 = 0
            for i, s in enumerate(S2):
                s2 += m[s] * 10 ** (len(S2) - i - 1)

            s3 = 0
            for i, s in enumerate(S3):
                s3 += m[s] * 10 ** (len(S3) - i - 1)

            if s1 + s2 == s3 and s1 > 0 and s2 > 0 and s3 > 0:
                print(s1)
                print(s2)
                print(s3)
                return

    print("UNSOLVABLE")


if __name__ == "__main__":
    main()
