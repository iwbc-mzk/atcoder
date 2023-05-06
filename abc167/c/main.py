n, m, x = map(int, input().split())
learn = [list(map(int, input().split())) for _ in range(n)]

start = 10 ** 10
result = start
for bit in range(2**n):
    total_price = 0
    progress = [0] * m
    for i, l in enumerate(learn):
        if bit >> i & 1:
            total_price += l[0]
            for j in range(m):
                progress[j] += l[j+1]
    if all(p >= x for p in progress):
        result = min(result, total_price)

print(result if result != start else -1)