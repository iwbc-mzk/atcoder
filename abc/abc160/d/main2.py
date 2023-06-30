from collections import defaultdict, deque


def main():
    N, X, Y = map(int, input().split())

    G = defaultdict(set)
    G[X].add(Y)
    G[Y].add(X)

    for i in range(1, N):
        G[i].add(i + 1)
        G[i + 1].add(i)

    distances = [0 for _ in range(N)]
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            # j - i: X-Y辺を通らない場合の距離
            # abs(X - i) + 1 + abs(j - Y): XY辺を通る場合の距離
            dist = min(j - i, abs(X - i) + 1 + abs(j - Y))
            distances[dist] += 1

    for i in range(1, N):
        print(distances[i])


if __name__ == "__main__":
    main()
