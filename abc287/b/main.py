n, m = map(int, input().split())
s, t = list(), set()
for _ in range(n):
    s.append(input()[-3:])
for _ in range(m):
    t.add(input())

ans = 0
for si in s:
    if si in t:
        ans += 1

print(ans)
