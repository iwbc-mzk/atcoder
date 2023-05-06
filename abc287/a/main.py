n = int(input())
total = 0
for _ in range(n):
    s = input()
    if s == "For":
        total += 1
    elif s == "Against":
        total -= 1

print("Yes" if total > 0 else "No")