n, m = map(int, input().split())
sc = []
for _ in range(m):
    s, c = map(int, input().split())
    sc.append((s, c))

for i in range(1000):
    i = str(i)
    if len(i) != n:
        continue

    flg = True
    for s, c in sc:
        if len(i) < s or i[s-1] != str(c):
            flg = False
            break
    if flg:
        print(i)
        break
else:
    print(-1)

        
