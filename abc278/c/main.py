from collections import defaultdict

def main():
    N, Q = map(int, input().split())
    graph = defaultdict(set)

    for _ in range(Q):
        T, A, B = input().split()
        
        if T == "1":
            graph[A].add(B)
        
        if T == "2":
            if B in graph[A]:
                graph[A].remove(B)

        if T == "3":
            if A in graph[B] and B in graph[A]:
                print("Yes")
            else:
                print("No")


if __name__ == "__main__":
    main()