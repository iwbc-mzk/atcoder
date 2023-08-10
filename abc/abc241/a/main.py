def main():
    A = list(map(int, input().split()))
    s = 0
    for _ in range(3):
        s = A[s]

    print(s)


if __name__ == "__main__":
    main()
