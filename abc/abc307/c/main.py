def get_blacks(l):
    blacks = set()
    for h, r in enumerate(l):
        for w, c in enumerate(r):
            if c == "#":
                blacks.add((h, w))

    return blacks


def norm(blacks):
    minh = min(x[0] for x in blacks)
    minw = min(x[1] for x in blacks)

    return {(h - minh, w - minw) for (h, w) in blacks}


def main():
    Ha, Wa = map(int, input().split())
    A = [list(input()) for _ in range(Ha)]

    Hb, Wb = map(int, input().split())
    B = [list(input()) for _ in range(Hb)]

    Hx, Wx = map(int, input().split())
    X = [list(input()) for _ in range(Hx)]

    A_norm = norm(get_blacks(A))
    B_norm = norm(get_blacks(B))
    X_norm = norm(get_blacks(X))

    for dh in range(-Hx, Hx):
        for dw in range(-Wx, Wx):
            b = {(h + dh, w + dw) for (h, w) in B_norm}
            u = A_norm | b
            if X_norm == norm(u):
                print("Yes")
                return
    else:
        print("No")


if __name__ == "__main__":
    main()
