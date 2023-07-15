def main():
    N = int(input())
    S = set(input() for _ in range(N))
    SS = S.copy()

    r = set()
    for s in S:
        s_inv = "".join(si for si in reversed(s))
        if s == s_inv:
            continue
        if s_inv in SS and s_inv not in r:
            SS.remove(s_inv)
            r.add(s_inv)
            r.add(s)

    print(len(SS))


if __name__ == "__main__":
    main()
