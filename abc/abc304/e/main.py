from queue import Queue


def main():
    N, M = map(int, input().split())

    gragh = {i: set() for i in range(1, N + 1)}
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)

    K = int(input())
    xy = set(tuple(map(int, input().split())) for _ in range(K))

    Q = int(input())

    visited = set()
    s_list = []
    i = 0
    idx_dict = {}
    for v in gragh:
        if v in visited:
            continue

        s = set()
        q = Queue()
        q.put(v)
        visited.add(v)
        while not q.empty():
            v = q.get()
            idx_dict[v] = i
            s.add(v)
            for vv in gragh[v]:
                if vv not in visited:
                    q.put(vv)
                    visited.add(vv)
        else:
            s_list.append(s)
            i += 1

    ng = set()
    for x, y in xy:
        ng.add((idx_dict[x], idx_dict[y]))

    for _ in range(Q):
        p, q = map(int, input().split())
        i1, i2 = idx_dict[p], idx_dict[q]
        if (i1, i2) in ng or (i2, i1) in ng:
            print("No")
        else:
            print("Yes")


if __name__ == "__main__":
    main()
