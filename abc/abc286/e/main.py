def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = [list(input()) for _ in range(N)]
    Q = int(input())

    INF = float("inf")
    dist = [[INF for _ in range(N + 1)] for _ in range(N + 1)]
    val = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
    for i in range(N + 1):
        dist[i][i] = 0
        val[i][i] = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == "Y":
                dist[i + 1][j + 1] = 1
                val[i + 1][j + 1] = A[j]

    for via in range(N + 1):
        for dep in range(N + 1):
            for dest in range(N + 1):
                d = dist[dep][via] + dist[via][dest]
                v = val[dep][via] + val[via][dest]
                if d < dist[dep][dest]:
                    dist[dep][dest] = d
                    val[dep][dest] = v
                elif (d == dist[dep][dest]) and (v > val[dep][dest]):
                    val[dep][dest] = v

    for _ in range(Q):
        U, V = map(int, input().split())

        if dist[U][V] == INF:
            print("Impossible")
        else:
            print(dist[U][V], val[U][V] + A[U - 1])


if __name__ == "__main__":
    main()
