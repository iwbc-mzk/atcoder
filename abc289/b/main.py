n, m = map(int, input().split())
a_list = list(map(int, input().split()))

numbers = list(range(1, n+1))
tmp = []
res = []
for num in numbers:
    tmp.insert(0, num)
    if num not in a_list:
        res += tmp
        tmp = []

print(*res)