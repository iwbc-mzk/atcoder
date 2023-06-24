def main():
    Ha, Wa = map(int, input().split())
    A = [list(input()) for _ in range(Ha)]

    Hb, Wb = map(int, input().split())
    B = [list(input()) for _ in range(Hb)]

    Hx, Wx = map(int, input().split())
    X = [list(input()) for _ in range(Hx)]

    black_a = 0
    for r in A:
        black_a += r.count("#")

    black_b = 0
    for r in B:
        black_b += r.count("#")

    black_x = 0
    for r in X:
        black_x += r.count("#")

    diff = abs(bl)



if __name__ == "__main__":
    main()
