n, k = map(int , input().split())
s = [input() for _ in range(n)]

sort = lambda x: x.split()
ss = s[:k]
for ssi in sorted(ss, key=sort):
    print(ssi)