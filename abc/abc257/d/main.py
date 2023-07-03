from collections import defaultdict, deque


def main():
    N = int(input())
    XYP = [list(map(int, input().split())) for _ in range(N)]

    left = 0
    right = 4 * 10**9
    while right - left > 1:
        S = (left + right) // 2
        G = defaultdict(set)
        for i1, (x1, y1, p1) in enumerate(XYP):
            for i2, (x2, y2, p2) in enumerate(XYP):
                if S * p1 >= abs(x1 - x2) + abs(y1 - y2):
                    G[i1].add(i2)

        ok = False
        for start in range(N):
            q = deque()
            q.append(start)
            visited = set()
            visited.add(start)
            while q:
                v = q.popleft()
                for vv in G[v]:
                    if vv not in visited:
                        q.append(vv)
                        visited.add(vv)

            if len(visited) == N:
                ok = True
                break

        if ok:
            right = S
        else:
            left = S

    print(right)


if __name__ == "__main__":
    main()
