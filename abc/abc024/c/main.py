import sys

sys.setrecursionlimit(10**9)


def main():
    N, D, K = map(int, input().split())
    LR = [tuple(map(int, input().split())) for _ in range(D)]
    ST = [tuple(map(int, input().split())) for _ in range(K)]

    for s, t in ST:
        for i, (l, r) in enumerate(LR, 1):
            if l <= s <= r:
                if l <= t <= r:
                    s = t
                else:
                    if t < l:
                        s = l
                    else:
                        s = r

            if s == t:
                print(i)
                break


if __name__ == "__main__":
    main()
