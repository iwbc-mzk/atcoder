def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    s = 0
    for a, b in zip(A, B):
        s += abs(a - b)

    if s <= K and abs(s - K) % 2 == 0:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
