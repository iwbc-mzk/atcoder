from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    C = defaultdict(list)
    for i, a in enumerate(A):
        C[a].append(i)

    ans = 0
    for n in range(1, N + 1):
        if n not in C:
            continue

        c = C[n]
        for j in range(len(c) - 1):
            diff = c[j + 1] - c[j] - 1
            ans += diff * (j + 1) * (len(c) - (j + 1))

    print(ans)


if __name__ == "__main__":
    main()
