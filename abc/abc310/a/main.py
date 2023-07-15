def main():
    N, P, Q = map(int, input().split())
    D = list(map(int, input().split()))

    D.sort()
    if P <= D[0] + Q:
        print(P)
    else:
        print(D[0] + Q)


if __name__ == "__main__":
    main()
