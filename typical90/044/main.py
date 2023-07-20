def main():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    s = 0
    for _ in range(Q):
        t, x, y = map(int, input().split())
        x = (x - 1 - s + N) % N
        y = (y - 1 - s + N) % N

        if t == 1:
            A[x], A[y] = A[y], A[x]
        elif t == 2:
            s += 1
        else:
            print(A[x])


if __name__ == "__main__":
    main()
