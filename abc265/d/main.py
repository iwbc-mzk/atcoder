def main():
    N, P, Q, R = map(int, input().split())
    A = list(map(int, input().split()))

    S = [0 for _ in range(N + 1)]
    for i in range(N + 1):
        if i == 0:
            S[0] = 0
        else:
            S[i] = S[i - 1] + A[i - 1]
    S_set = set(S)
    
    for sx in S:
        sy = sx + P
        if sy in S_set:
            sz = sy + Q
            if sz in S_set:
                sw = sz + R
                if sw in S_set:
                    print("Yes")
                    return
    else:
        print("No")


if __name__ == "__main__":
    main()