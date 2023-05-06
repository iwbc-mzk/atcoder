from collections import defaultdict
import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())

g = defaultdict(set)

for _ in range(m):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

def dfs(gragh: dict, seen: set, vartex: int):
    seen.add(vartex)
    for v in gragh[vartex]:
        if v not in seen:
            dfs(gragh, seen, v)

seen_set = set()
join_ele_cnt = 0
for start in range(1, n+1):
    if start not in seen_set:
        join_ele_cnt += 1
        dfs(g, seen_set, start)
        

print(m - n + join_ele_cnt)