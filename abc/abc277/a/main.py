def main():
    N, X = input().split()
    P = input().split()

    l = []
    for i, p in enumerate(P):
        if p == X:
            l.append(str(i+1))

    print(" ".join(l))


if __name__ == "__main__":
    main()