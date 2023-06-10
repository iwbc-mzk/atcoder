from collections import defaultdict
from queue import Queue


def main():
    N, M, K = map(int, input().split())
    gragh = defaultdict(set)
    for _ in range(M):
        a, b = map(int, input().split())
        gragh[a].add(b)
        gragh[b].add(a)

    PH = defaultdict(int)
    for _ in range(K):
        p, h = map(int, input().split())
        PH[p] = h

    ans = [0 for _ in range(N + 1)]
    for p, h in PH.items():
        q = Queue()
        q.put((p, h + 1))
        ans[p] = h
        while not q.empty():
            v, d = q.get()
            if d < ans[v]:
                continue
            ans[v] = d

            if d - 1 == 0:
                continue

            for vv in gragh[v]:
                dd = d - 1
                if vv in PH:
                    dd = max(dd, PH[vv] + 1)
                if dd > ans[vv]:
                    q.put((vv, dd))

    cnt = 0
    ans_idx = []
    for i, a in enumerate(ans):
        if a > 0:
            cnt += 1
            ans_idx.append(i)
    print(cnt)
    print(*ans_idx)


if __name__ == "__main__":
    main()
