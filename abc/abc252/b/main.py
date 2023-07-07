def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A = [(a, i) for i, a in enumerate(A, 1)]
    A.sort()
    B = set(map(int, input().split()))

    m = A[-1][0]
    while m == A[-1][0]:
        a, i = A.pop()
        if i in B:
            print("Yes")
            return
    else:
        print("No")


if __name__ == "__main__":
    main()
