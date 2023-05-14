def main():
    H, W = map(int, input().split())
    A = [map(int, input().split()) for _ in range(H)]

    alpha = list(".ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    for a in A:
        S = ""
        for ai in a:
            S += alpha[ai]
        print(S)

if __name__ == "__main__":
    main()