from math import gcd

def main():
    T = int(input())
    NDK = [tuple(map(int, input().split())) for _ in range(T)]

    for N, D, K in NDK:
        K -= 1
        g = gcd(N, D)
        cycle = N // g
        print(K // cycle + D * (K % cycle) % N)


if __name__ == "__main__":
    main()