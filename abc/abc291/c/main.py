from collections import defaultdict

n = int(input())
s = input()

his = defaultdict(set)
x, y = 0, 0
his[x].add(y)
ans = "No"
for si in s:
    if si == "R":
        x += 1
    elif si == "L":
        x -= 1
    elif si == "U":
        y += 1
    elif si == "D":
        y -= 1

    if y in his[x]:
        ans = "Yes"
        break
    his[x].add(y)

print(ans)