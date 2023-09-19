import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    X, Y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    ans = 0
    t = 0
    a, b = -1, -1
    a_flg = True
    while True:
        if a_flg:
            if not A:
                break

            while a < t:
                if not A:
                    break
                a = A.pop()
            else:
                t = a + X
                a_flg = False
        else:
            if not B:
                break

            while b < t:
                if not B:
                    break
                b = B.pop()
            else:
                t = b + Y
                a_flg = True
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
