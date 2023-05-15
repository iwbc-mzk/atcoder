def main():
    N, W = map(int, input().split())

    S = []
    T = []
    P = []
    for _ in range(N):
        s, t, p = map(int, input().split())
        S.append(s)
        T.append(t)
        P.append(p)

    max_t = max(T)
    table = [0 for _ in range(max_t + 1)]
    for s, t, p in zip(S, T, P):
        table[s] += p
        table[t] -= p

    for i in range(len(table)):
        if i > 0:
            table[i] += table[i - 1]
            
        if table[i] > W:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()