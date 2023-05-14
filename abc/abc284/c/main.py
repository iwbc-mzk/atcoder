from collections import defaultdict

visited = set()

def rec(graph, n):
    visited.add(n)
    for v in graph[n]:
        if v in visited:
            continue

        rec(graph, v)


def main():
    N, M = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].add(v)
        graph[v].add(u)

    result = 0
    for n in range(1, N+1):
        if n in visited:
            continue
        else:
            rec(graph, n)
            result += 1

    print(result)

if __name__ == "__main__":
    main()