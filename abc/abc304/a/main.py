def main():
    N = int(input())
    SA = [tuple(input().split()) for _ in range(N)]

    min_idx = 0
    min_age = 10**9 + 1
    for i, (s, a) in enumerate(SA):
        if int(a) < min_age:
            min_idx = i
            min_age = int(a)

    for i in range(N):
        print(SA[(min_idx + i) % N][0])


if __name__ == "__main__":
    main()
