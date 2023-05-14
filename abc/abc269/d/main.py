from queue import LifoQueue

def main():
    N = int(input())
    blacks = {tuple(map(int, input().split())) for _ in range(N)}

    visited = set()
    ans = 0
    comb = [(-1, -1), (-1, 0), (0, -1), (0, 1), (1, 0), (1, 1)]
    for b in blacks:
        q = LifoQueue()
        if b not in visited:
            q.put(b)
            ans += 1

        while not q.empty():
            v = q.get()
            visited.add(v)

            for c1, c2 in comb:
                vv = (v[0] + c1, v[1] + c2)
                if vv in blacks and vv not in visited:
                    q.put(vv)

    print(ans)

if __name__ == "__main__":
    main()