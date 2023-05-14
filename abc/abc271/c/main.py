def main():
    N = int(input())

    A_set = set(map(int, input().split()))
    A = list(A_set)
    A.sort()
    
    remaind = N - len(A_set)
    sold = set()
    for vol in range(1, 3 * 10 ** 5 + 1):
        if vol in A_set:
            continue
        
        if remaind >= 2:
            sell_cnt = 2
            remaind -= 2
        else:
            sell_cnt = remaind
            remaind = 0

            for i in reversed(range(len(A) - len(sold))):
                if A[i] <= vol:
                    break

                if i not in sold:
                    sold.add(i)
                    A_set.remove(A[i])
                    sell_cnt += 1
                
                if sell_cnt == 2:
                    break

        if sell_cnt == 2:
            continue
        else:
            print(vol - 1)
            break
    else:
        print(vol)
       


if __name__ == "__main__":
    main()