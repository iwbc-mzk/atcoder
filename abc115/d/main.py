from collections import defaultdict

def cnt(level: int, x: int, total: list, patty: list):
    if level == 0:
        return 1
    
    if x == 1:
        return 0
    elif 1 < x <= total[level-1] + 1:
        return cnt(level-1, x-1, total, patty)
    elif x == total[level-1] + 2:
        return patty[level-1] + 1
    elif total[level-1] + 2 < x < 2 * total[level-1] + 2:
        return cnt(level-1, x-total[level-1]-2, total, patty) + patty[level-1] + 1
    else:
        return 2 * patty[level-1] + 1


n, x = map(int, input().split())

total = [0] * n
patty = [0] * n
for i in range(n):
    if i == 0:
        total[0] = 1
        patty[0] = 1
    else:
        total[i] = 2 * total[i-1] + 3
        patty[i] = 2 * patty[i-1] + 1

print(cnt(n, x, total, patty))