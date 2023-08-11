def main():
    N = int(input())
    S = input()

    A = []
    for s in S:
        A.append(s)
        if A[-3:] == ["f", "o", "x"]:
            for _ in range(3):
                A.pop()

    print(len(A))


if __name__ == "__main__":
    main()
