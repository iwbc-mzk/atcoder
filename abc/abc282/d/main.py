from collections import defaultdict
from queue import Queue

WHITE, BLACK = 0, 1

def comb(n):
    return n * (n - 1) // 2

def main():
    N, M = map(int, input().split())
    gragh = defaultdict(set)

    for _ in range(M):
        u, v = map(int, input().split())
        u, v = u-1, v-1
        gragh[u].add(v)
        gragh[v].add(u)

    colors = [-1 for _ in range(N)]
    is_bipartite = True
    ng_pair_num = 0
    for i in range(N):
        if colors[i] != -1:
            continue

        white_num, black_num = 0, 0

        que = Queue()
        que.put(i)
        colors[i] = WHITE
        while not que.empty():
            u = que.get()
            if colors[u] == WHITE:
                white_num += 1
            elif colors[u] == BLACK:
                black_num += 1

            next_color = 1 - colors[u]
            for v in gragh[u]:
                if colors[v] == -1:
                    que.put(v)
                    colors[v] = next_color
                else:
                    if colors[v] != next_color:
                        is_bipartite = False
                        break

        if not is_bipartite:
            break

        ng_pair_num += comb(white_num) + comb(black_num)
    
    if is_bipartite:
        print(comb(N) - M - ng_pair_num)
    else:
        print(0)


if __name__ == "__main__":
    main()