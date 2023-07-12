from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    G = defaultdict(set)
    for i, a in enumerate(A, 1):
        G[a].add(2 * i)
        G[a].add(2 * i + 1)

    H = [0 for _ in range(2 * N + 1)]
    for n in range(1, 2 * N + 2):
        for v in G[n]:
            H[v - 1] = H[n - 1] + 1

    for h in H:
        print(h)


if __name__ == "__main__":
    main()
