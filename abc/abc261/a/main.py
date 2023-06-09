def main():
    L1, R1, L2, R2 = map(int, input().split())

    L = max(L1, L2)
    R = min(R1, R2)
    if R < L:
        print(0)
    else:
        print(R - L)


if __name__ == "__main__":
    main()
