from itertools import combinations_with_replacement

def calc_score(seq):
    score = 0
    for a, b, c, d in pairs:
        if seq[b-1] - seq[a-1] == c:
            score += d

    return score

n, m, q = map(int, input().split())
pairs = [list(map(int, input().split())) for _ in range(q)]

max_score = 0
comb = combinations_with_replacement(range(1, m+1), n)
for seq in comb:
    max_score = max(max_score, calc_score(sorted(seq)))

print(max_score)