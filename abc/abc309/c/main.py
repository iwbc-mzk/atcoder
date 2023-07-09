def main():
    N, K = map(int, input().split())

    AB = []
    s = 0
    for _ in range(N):
        a, b = map(int, input().split())
        AB.append((a, b))
        s += b

    if s <= K:
        print(1)
        return

    AB.sort()
    for a, b in AB:
        s -= b
        if s <= K:
            print(a + 1)
            return


if __name__ == "__main__":
    main()
