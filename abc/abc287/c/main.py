from collections import defaultdict
from queue import Queue

def main():
    N, M = map(int, input().split())
    gragh = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)

    start = None
    for u, v in gragh.items():
        if len(v) == 1:
            start = u
            break
    
    ans = True if start else False
    if start:
        q = Queue()
        q.put(start)
        visited = set()
        pre_t = -1
        while not q.empty():
            t = q.get()
            if t in visited:
                ans = False
                break

            visited.add(t)

            for n in gragh[t]:
                if n != pre_t:
                    q.put(n)
            pre_t = t
        else:
            ans = len(visited) == N

    print("Yes" if ans else "No")
    

if __name__ == "__main__":
    main()