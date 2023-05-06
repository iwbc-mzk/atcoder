from collections import defaultdict
from queue import Queue
 
def main():
    N, M = map(int, input().split())
    
    gragh = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        gragh[u].add(v)
        gragh[v].add(u)
 
    K = int(input())
    P = []
    D = []
    for _ in range(K):
        p, d = map(int, input().split())
        P.append(p)
        D.append(d)
 
 
    distances = {}
    for n in range(1, N + 1):
        q = Queue()
        q.put(n)
 
        visited = set()
        visited.add(n)
 
        distance = [0 for _ in range(N)]
        distance[n - 1] = 0
 
        while not q.empty():
            v = q.get()
            not_visited = gragh[v] - visited
            for next_point in not_visited:
                distance[next_point - 1] = distance[v - 1] + 1
                q.put(next_point)
                visited.add(next_point)
        
        distances[n] = distance
    
    T = ["1" for _ in range(N)]
    for p, d in zip(P, D):
        for i, dis in enumerate(distances[p]):
            if dis < d:
                T[i] = "0"
    
    ans = "1" in T
    for p, d in zip(P, D):
        black_flg = False
        for i, dis in enumerate(distances[p]):
            if dis < d:
                ans &= T[i] == "0"
            if dis == d:
                black_flg |= T[i] == "1"
 
        ans &= black_flg
 
    print("Yes" if ans else "No")
    if ans:
        print("".join(T))
 
 
if __name__ == "__main__":
    main()