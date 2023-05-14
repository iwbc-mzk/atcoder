from itertools import combinations

def main():
    H1, W1 = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H1)]
    H2, W2 = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(H2)]

    comb_h = list(combinations(range(H1), H1 - H2))
    comb_w = list(combinations(range(W1), W1 - W2))

    for del_h in comb_h:
        for del_w in comb_w:
            ha = 0
            flg = True
            for hb in range(H2):
                while ha in del_h:
                        ha += 1

                wa = 0
                for wb in range(W2):
                    while wa in del_w:
                        wa += 1
                    
                    try:
                        if A[ha][wa] != B[hb][wb]:
                            flg = False
                            break
                    except:
                        pass
                    wa += 1
                if not flg:
                    break
                ha += 1
            else:
                print("Yes")
                return
    else:
        print("No")
        return
                    




if __name__ == "__main__":
    main()