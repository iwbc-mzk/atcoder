from collections import defaultdict

n, m = map(int, input().split())

ss = []
for i in range(m):
    c = input()
    s = list(map(int, input().split()))
    ss.append(s)

cnt = 0
for i in range(2**m):
    t_set = set()
    for idx, s in enumerate(ss):
        if i >> idx & 1:
            t_set.update(s)

    for nn in range(1, n+1):
        if nn not in t_set:
            break
    else:
        cnt += 1

print(cnt)