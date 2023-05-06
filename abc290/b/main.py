n, k = map(int, input().split())
s = input()

cnt = 0
result = ""
for idx, si in enumerate(s):
    result += si
    if si == "o":
        cnt += 1

    if cnt == k:
        result += "x" * (n - idx - 1)
        break

print(result)
