import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = list(map(int, input().split()))

    B = [0]
    C = {0: 1}
    for a in A:
        v = B[-1] + a
        B.append(v)
        if v in C:
            C[v] += 1
        else:
            C[v] = 1

    ans = 0
    for _, v in C.items():
        if v > 1:
            ans += v * (v - 1) // (2 * 1)

    print(ans)


if __name__ == "__main__":
    main()
