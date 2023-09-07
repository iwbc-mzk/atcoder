import sys

sys.setrecursionlimit(10**9)


def main():
    K = int(input())
    S = input()
    T = input()

    C1 = [0 for _ in range(9)]
    C2 = [0 for _ in range(9)]
    for s, t in zip(S, T):
        if s != "#":
            C1[int(s) - 1] += 1
        if t != "#":
            C2[int(t) - 1] += 1

    win = 0
    for i in range(1, 10):
        if C1[i - 1] + C2[i - 1] >= K:
            continue

        C1[i - 1] += 1

        for j in range(1, 10):
            if C1[j - 1] + C2[j - 1] >= K:
                continue

            C2[j - 1] += 1

            takahashi, aoki = 0, 0
            for k, (c1, c2) in enumerate(zip(C1, C2), 1):
                takahashi += k * 10**c1
                aoki += k * 10**c2

            if takahashi > aoki:
                if i == j:
                    c = K - C1[i - 1] - C2[j - 1] + 2
                    win += c * (c - 1)
                else:
                    c1 = K - C1[i - 1] - C2[i - 1] + 1
                    c2 = K - C2[j - 1] - C1[j - 1] + 1
                    win += c1 * c2

            C2[j - 1] -= 1
        C1[i - 1] -= 1

    total = (9 * K - 8) * (9 * K - 9)
    print(win / total)


if __name__ == "__main__":
    main()
