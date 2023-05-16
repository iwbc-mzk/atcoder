import math

def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())

    M = [A, B, C, D, E]

    neck = min(M)

    print(math.ceil(N / neck) + 4)


if __name__ == "__main__":
    main()