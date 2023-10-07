import sys

sys.setrecursionlimit(10**9)


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    S = [list(input()) for _ in range(N)]

    scores = []
    for i, s in enumerate(S):
        score = i + 1
        for j, sj in enumerate(s):
            if sj == "o":
                score += A[j]

        scores.append(score)

    max_score = max(scores)

    AA = [(a, i) for i, a in enumerate(A)]
    AA.sort(reverse=True)
    for i, s in enumerate(S):
        score = scores[i]
        c = 0
        j = 0
        while score < max_score:
            a, k = AA[j]
            if s[k] == "x":
                score += a

                c += 1
            j += 1

        print(c)


if __name__ == "__main__":
    main()
