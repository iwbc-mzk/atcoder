import sys
sys.setrecursionlimit(10 ** 8)

def rec(i, A, price, ptn: set, limit):
    if len(ptn) > limit:
        return
    
    rec(i, A, price + A[i], ptn, limit)
    ptn.add(price + A[i])

    rec(i + 1, A, price, ptn, limit)

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()

    ptn = set()
    rec(0, A, 0, ptn, K)
    print(list(ptn).sort()[K-1])
    


if __name__ == "__main__":
    main()