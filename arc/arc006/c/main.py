import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    W = [int(input()) for _ in range(N)]

    H = []
    for w in W:
        min_h = float("inf")
        min_hi = -1
        for i, h in enumerate(H):
            if w <= h < min_h:
                min_h = h
                min_hi = i

        if min_hi == -1:
            H.append(w)
        else:
            H[min_hi] = w

    print(len(H))


if __name__ == "__main__":
    main()
