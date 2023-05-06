from itertools import combinations

def main():
    N, M = map(int, input().split())
    S = [list(input()) for _ in range(N)]

    cmb = combinations(S, 2)
    result = 0
    for a, b in cmb:
        for m in range(M):
            if a[m] != "o" and b[m] != "o":
                break
        else:
            result += 1

    print(result)


if __name__ == "__main__":
    main()