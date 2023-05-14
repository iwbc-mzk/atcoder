def main():
    A, B, C, D, E, F = map(int, input().split())

    print(((A * B * C) - (D * E * F)) % 998244353)


if __name__ == "__main__":
    main()