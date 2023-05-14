from itertools import combinations
from collections import defaultdict

n = int(input())

ss = ["".join(sorted(input())) for _ in range(n)]
d = defaultdict(int)
for s in ss:
    d[s] += 1

cnt = 0
for v in d.values():
    cnt += v*(v-1)//2

print(cnt)
    