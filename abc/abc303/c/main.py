def main():
    N, M, H, K = map(int, input().split())
    S = input()
    C = set(tuple(map(int, input().split())) for _ in range(M))

    pos = (0, 0)
    hp = H
    for s in S:
        if s == "R":
            pos = (pos[0] + 1, pos[1])
        if s == "L":
            pos = (pos[0] - 1, pos[1])
        if s == "U":
            pos = (pos[0], pos[1] + 1)
        if s == "D":
            pos = (pos[0], pos[1] - 1)

        hp -= 1
        if hp < 0:
            print("No")
            break

        if pos in C and hp < K:
            C.remove(pos)
            hp = K
    else:
        print("Yes")


if __name__ == "__main__":
    main()
