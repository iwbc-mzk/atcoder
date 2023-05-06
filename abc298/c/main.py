from collections import defaultdict

def main():
    N = int(input())
    Q = int(input())

    D = defaultdict(lambda: defaultdict(int))
    DD = defaultdict(set)
    for i in range(Q):
        m, i, *j = map(int, input().split())
        if m == 1:
            j = j[0]
            D[j][i] += 1
            DD[i].add(j)
        if m == 2:
            for idx1, k in enumerate(sorted(D[i].keys())):
                for idx2 in range(D[i][k]):
                    if idx1 != 0 or idx2 != 0:
                        print(" ", end="")
                    print(k, end="")
            print()
        if m == 3:
            print(*sorted(DD[i]))




if __name__ == "__main__":
    main()