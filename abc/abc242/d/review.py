def main():
    S = input()
    Q = int(input())

    C = {"A": "BC", "B": "CA", "C": "AB"}

    for _ in range(Q):
        t, k = map(int, input().split())

        def s(t, k):
            if t == 0:
                return S[k]
            if k == 0:
                return chr(ord("A") + ((ord(S[0]) - ord("A")) + t % 3) % 3)
            return C[s(t - 1, k // 2)][k % 2]

        print(s(t, k - 1))


if __name__ == "__main__":
    main()
