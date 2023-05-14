def main():
    N, A, B = map(int, input().split())
    C = list(map(int, input().split()))
    for i in range(N):
        if A + B == C[i]:
            print(i + 1)
            break


if __name__ == "__main__":
    main()