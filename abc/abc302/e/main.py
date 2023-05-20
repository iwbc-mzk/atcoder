from collections import defaultdict

def main():
    N, Q = map(int, input().split())
    gragh = defaultdict(set)
    for q in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            u, v = query[1:]
            gragh[u].add(v)
            gragh[v].add(u)


if __name__ == "__main__":
    main()