from queue import Queue
from collections import defaultdict


def main():
    N, M = map(int, input().split())

    gragh = defaultdict(set)
    dg = defaultdict(int)
    for _ in range(M):
        a, b, c, d = input().split()
        a = int(a)
        c = int(c)
        gragh[a].add(c)
        gragh[c].add(a)
        dg[a] += 1
        dg[c] += 1

    n_loop = 0
    n_no_loop = 0
    visited = set()
    for start in range(1, N + 1):
        if start in visited:
            continue

        q = Queue()
        q.put(start)
        visited.add(start)

        loop_flg = True
        while not q.empty():
            v = q.get()
            loop_flg &= dg[v] == 2
            for vv in gragh[v]:
                if vv not in visited:
                    q.put(vv)
                    visited.add(vv)                    

        if loop_flg:
            n_loop += 1
        else:
            n_no_loop += 1

    print(n_loop, n_no_loop)


if __name__ == "__main__":
    main()
