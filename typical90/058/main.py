def convert(v: int) -> int:
    t = 0
    vv = v
    for i in reversed(range(5)):
        t += vv // 10**i
        vv -= (vv // 10**i) * 10**i
    v += t
    v %= 10**5
    return v


def main():
    N, K = map(int, input().split())

    flags = [-1 for _ in range(10**5)]
    v = N
    i = 0
    while flags[v] == -1 and i < K:
        flags[v] = i
        v = convert(v)
        i += 1

    if i == K:
        print(v)
        return
    else:
        loop_s = flags[v]
        loop_end = i - 1
        c = loop_end - loop_s + 1

        K -= loop_s
        remain = K % c

        for _ in range(remain):
            v = convert(v)

        print(v)


if __name__ == "__main__":
    main()
