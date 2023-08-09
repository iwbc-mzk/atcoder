import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    AS = set()
    BS = set()
    ans1 = 0
    for a, b in zip(A, B):
        if a == b:
            ans1 += 1

        AS.add(a)
        BS.add(b)

    AB = AS.intersection(BS)
    ans2 = len(AB) - ans1

    print(ans1)
    print(ans2)


if __name__ == "__main__":
    main()
