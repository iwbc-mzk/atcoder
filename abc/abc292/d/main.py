from collections import defaultdict
from queue import Queue

def main():
    N, M = map(int, input().split())

    if N != M:
        print("No")
        return

    gragh = defaultdict(list)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].append(v)
        gragh[v].append(u)

    visited = set()
    for x in range(1, N + 1):
        q = Queue()
        if x in visited:
            continue

        q.put(x)
        visited.add(x)
        line = 0
        top = set()
        top.add(x)
        while not q.empty():
            v = q.get()
            for vv in gragh[v]:
                top.add(vv)
                if vv not in visited:
                    q.put(vv)
                    visited.add(vv)
                
                line += 1
        
        if line // 2 != len(top):
            print("No")
            return
    else:
        print("Yes")
        return
    


if __name__ == "__main__":
    main()