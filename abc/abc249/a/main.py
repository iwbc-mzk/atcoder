def main():
    A, B, C, D, E, F, X = map(int, input().split())

    takahashi = 0
    aoki = 0
    for x in range(1, X + 1):
        if (x - 1) % (A + C) <= A:
            takahashi += B

        if (x - 1) % (D + F) <= D:
            aoki += E

    if takahashi > aoki:
        print("Takahashi")
    elif takahashi < aoki:
        print("Aoki")
    else:
        print("Draw")


if __name__ == "__main__":
    main()
