from statistics import mean

n = int(input())
scores = list(map(int, input().split()))
scores.sort()

print(float(mean(scores[n:len(scores)-n])))
