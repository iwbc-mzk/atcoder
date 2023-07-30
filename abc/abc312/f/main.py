import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())

    T1 = []
    T2 = []
    T3 = []
    for _ in range(N):
        t, x = map(int, input().split())
        if t == 0:
            T1.append(x)
        elif t == 1:
            T2.append(x)
        else:
            T3.append(x)

    T1.sort(reverse=True)
    T2.sort(reverse=True)
    T3.sort(reverse=True)

    if len(T1) >= M:
        ans = sum(T1[:M])
        t = 0
        t3_i = 0
        t2_i = 0
        t1_i = 0
        while True:
            if t == 0:
                t += T3[t3_i]
                t3_i += 1
                if T2[t2_i] > T1[t1_i] + T1[t1_i + 1]:
                    t1_i += 2
                    t2_i += 1
                else:
                    break
            else:
                if T2[t2_i] + T2[t2_i + 1] > T1[t1_i] + T1[t1_i + 1]:
                    t1_i += 2
                    t2_i += 2
                else:
                    break

    else:
        ans = sum(T1)
        t = 0
        m = M - len(T1)
        t3_i = 0
        t2_i = 0
        t1_i = len(T1) - 1
        while True:
            if t == 0:
                if t3_i == len(T3):
                    break

                t += T3[t3_i]
                t3_i += 1
                m -= 1
            else:
                if m == 0:
                    if T2[t2_i] > T1[t1_i]:
                        ans += T2[t2_i] - T1[t1_i]
                        t1_i -= 1
                        t2_i += 1
                    else:
                        break
                else:
                    ans += T2[t2_i]
                    t2_i += 1
                    m -= 1

    print(ans)


if __name__ == "__main__":
    main()
