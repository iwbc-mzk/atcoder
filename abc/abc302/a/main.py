def main():
    A, B = map(int, input().split())
    if A % B:
        print(A // B + 1)
    else:
        print(A // B)


if __name__ == "__main__":
    main()