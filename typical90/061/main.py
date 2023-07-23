def main():
    Q = int(input())

    u = []
    l = []
    for _ in range(Q):
        t, x = map(int, input().split())
        if t == 1:
            u.append(x)
        elif t == 2:
            l.append(x)
        else:
            if x <= len(u):
                print(u[-x])
            else:
                x -= len(u)
                print(l[x - 1])


if __name__ == "__main__":
    main()
