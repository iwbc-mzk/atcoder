import sys

sys.setrecursionlimit(10**9)


def main():
    T = int(input())

    for _ in range(T):
        a, s = map(int, input().split())
        if s < 2 * a:
            print("No")
            continue
        else:
            t = s - 2 * a
            for i in range(60, -1, -1):
                if a >> i & 1:
                    continue
                else:
                    if 2**i <= t:
                        t -= 2**i

            if t == 0:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()
