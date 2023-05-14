from collections import defaultdict

def main():
    N, M = map(int, input().split())
    graph = defaultdict(set)
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A].add(B)
        graph[B].add(A)

    for i in range(1, N+1):
        cities = graph[i]
        cities_asc = sorted(cities)
        print(len(cities), " ".join(map(str, cities_asc)))


if __name__ == "__main__":
    main()