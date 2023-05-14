from itertools import permutations

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]
    T = {input() for _ in range(M)}

    def DFS(i, S_prime, s, c, ans):
        if i == N:
            if s not in T:
                ans.append(s)
            return

        for j in range(c + 1):
            s_next = s + "_" * (j + 1) + S_prime[i]
            DFS(i + 1, S_prime, s_next, c - j, ans)

    _cnt = 16 - (N - 1 + sum(map(len, S)))
    perm = permutations(range(N), N)
    ans = []
    for p in perm:
        S_prime = [S[i] for i in p]
        DFS(1, S_prime, S_prime[0], _cnt, ans)
    
    for a in ans:
        if 3 <= len(a) <= 16:
            print(a)
            break
    else:
        print(-1)


if __name__ == "__main__":
    main()