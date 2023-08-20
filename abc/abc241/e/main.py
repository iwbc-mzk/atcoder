def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    # ループを見つける
    loop = []
    loop_s = None
    loop_x = 0
    x = 0
    s = set()
    while True:
        t = x % N
        if t in s:
            if loop_s == t:
                break
            loop.append(t)
            loop_x += A[t]
            if loop_s is None:
                loop_s = t
        else:
            s.add(t)

        x += A[t]

    # ループを用いて計算
    k = K
    x = 0
    while k > 0:
        t = x % N
        if t != loop[0]:
            x += A[t]
            k -= 1
        else:
            break

    if k > 0:
        x += k // len(loop) * loop_x
        k = k % len(loop)
        for i in range(k):
            x += A[loop[i]]

    print(x)


if __name__ == "__main__":
    main()
