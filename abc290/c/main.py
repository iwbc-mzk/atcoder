n, k = map(int, input().split())
a_list = set(map(int, input().split()))

m = 0
for i in range(k):
    if i not in a_list:
        m = i
        break
else:
    m = k

print(m)
