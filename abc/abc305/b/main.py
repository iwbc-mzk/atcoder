def main():
    p, q = input().split()
    D = {"A": 0, "B": 3, "C": 4, "D": 8, "E": 9, "F": 14, "G": 23}
    print(abs(D[p] - D[q]))


if __name__ == "__main__":
    main()
