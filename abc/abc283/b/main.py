def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            A[q[1]-1] = q[2]
        elif q[0] == 2:
            print(A[q[1]-1])


if __name__ == "__main__":
    main()