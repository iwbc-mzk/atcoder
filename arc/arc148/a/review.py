from math import gcd


def main():
    N = int(input())
    A = list(map(int, input().split()))
    AA = [abs(A[i] - A[i + 1]) for i in range(N - 1)]

    m = 0
    for a in AA:
        m = gcd(a, m)

    if m == 1:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()
