import sys

sys.set_int_max_str_digits(0)
sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = input()
    B = input()

    MOD = 998244353

    AA, BB = [], []
    for a, b in zip(A, B):
        if a > b:
            a, b = b, a
        AA.append(a)
        BB.append(b)

    m = (int("".join(AA)) % MOD) * (int("".join(BB)) % MOD)
    m %= MOD

    print(m)


if __name__ == "__main__":
    main()
