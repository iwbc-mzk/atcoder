def main():
    N, K, Q = map(int, input().split())
    A = list(map(int, input().split()))
    L = list(map(int, input().split()))

    pos = {}
    for i, a in enumerate(A):
        pos[i + 1] = a

    for l in L:
        if l + 1 in pos:
            if pos[l + 1] - pos[l] > 1:
                pos[l] = min(pos[l] + 1, N)
        else:
            pos[l] = min(pos[l] + 1, N)

    print(*pos.values())


if __name__ == "__main__":
    main()
