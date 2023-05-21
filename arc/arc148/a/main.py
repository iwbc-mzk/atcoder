from math import gcd

def main():
    N = int(input())
    A = list(map(int, input().split()))

    dA = [A[i] - A[i + 1] for i in range(N - 1)]
    # m = gcd(*dA)
    m = 0
    for da in dA:
        m = gcd(m, da)
        
    if m == 1:
        print(2)
    else:
        print(1)


if __name__ == "__main__":
    main()