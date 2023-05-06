from collections import defaultdict
from queue import Queue

def main():    
    N, X, Y = map(int, input().split())

    gragh = defaultdict(set)
    for _ in range(N - 1):
        U, V = map(int, input().split())
        gragh[U].add(V)
        gragh[V].add(U)

    q = Queue()
    q.put(X)
    visited = defaultdict(bool)
    parents = defaultdict(int)
    parents[X] = -1
    while not q.empty():
        v = q.get()
        visited[v] = True
        if v == Y:
            break

        for vv in gragh[v]:
            if not visited[vv]:
                q.put(vv)
                parents[vv] = v

    y = Y
    ans = []
    while parents[y] != -1:
        ans.append(y)
        y = parents[y]
    else:
        ans.append(X)
    
    print(*ans[::-1])



if __name__ == "__main__":
    main()