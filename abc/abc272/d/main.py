from queue import Queue

def main():
    N, M = map(int, input().split())
    mat = [(a, b) for a in range(1, N+1) for b in range(1, N+1)]
    
    start = (1, 1)
    options = set()
    for dest in mat:
        x, y = dest[0] - start[0], dest[1] - start[1]
        if x ** 2 + y ** 2 == M:
            options.add((x, y))

    ans = [[-1 for _ in range(N)].copy() for _ in range(N)]
    ans[0][0] = 0
    q = Queue()
    q.put((start[0], start[1], 0))
    while not q.empty():
        r, c, cnt = q.get()
        for opt in options:
            for pmr, pmc in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
                nr, nc = r + pmr * opt[0], c + pmc * opt[1]
                if 1 <= nr <= N and 1 <= nc <= N:
                    if ans[nr-1][nc-1] == -1 or ans[nr-1][nc-1] > cnt + 1:
                        ans[nr-1][nc-1] = cnt + 1
                        q.put((nr, nc, cnt + 1))

    for a in ans:
        print(*a)
    

if __name__ == "__main__":
    main()