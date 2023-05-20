from itertools import permutations

def main():
    N, M = map(int, input().split())
    S = [input() for _ in range(N)]

    perm = permutations(S, len(S))
    for ss in perm: # 5 * 10 ** 4
        for i in range(N - 1):
            cnt = 0
            for k in range(M):
                if ss[i][k] != ss[i + 1][k]:
                    cnt += 1

            if cnt != 1:
                break
        else:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()