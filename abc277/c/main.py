from collections import defaultdict
from queue import Queue



def main():
    N = int(input())
    gragh = defaultdict(set)
    for _ in range(N):
        A, B = map(int, input().split())
        gragh[A].add(B)
        gragh[B].add(A)

    start = 1
    VISITED = set()
    q = Queue()
    q.put(start)
    max_floor = 0
    while not q.empty():
        n = q.get()
        if n in VISITED:
            continue

        VISITED.add(n)
        max_floor = max(max_floor, n)

        for i in gragh[n]:
            q.put(i)

    print(max_floor)


if __name__ == "__main__":
    main()