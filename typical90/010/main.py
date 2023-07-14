def main():
    N = int(input())

    C1 = [0]
    C2 = [0]
    for n in range(N):
        C, P = map(int, input().split())
        if C == 1:
            C1.append(C1[n] + P)
            C2.append(C2[n])
        else:
            C1.append(C1[n])
            C2.append(C2[n] + P)

    Q = int(input())
    for _ in range(Q):
        L, R = map(int, input().split())
        print(C1[R] - C1[L - 1], C2[R] - C2[L - 1])


if __name__ == "__main__":
    main()
