def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    even = map(str, filter(lambda x: x % 2 == 0, A))
    print(" ".join(even))


if __name__ == "__main__":
    main()