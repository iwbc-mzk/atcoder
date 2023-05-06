from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 9)

seen = defaultdict(bool)
finished = defaultdict(bool)
has_cycle = False

def has_cycle(graph, p):
    flg = False
    seen[p] = True
    for n in graph[p]:
        if seen[n] and not finished[n]:
            return True
        
        if seen[n]:
            continue

        flg |= has_cycle(graph, n)

    finished[p] = True
    return flg
    

def main():
    N = int(input())

    graph = defaultdict(set)
    start = None
    for _ in range(N):
        Si, Ti = input().split()
        graph[Si].add(Ti)
        if not start:
            start = Si

    result = False
    for s in list(graph.keys()):
        if seen[s]:
            continue
        result |= has_cycle(graph, s)

    print("Yes" if not result else "No")



if __name__ == "__main__":
    main()