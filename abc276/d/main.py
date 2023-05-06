from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))

    min_2, min_3 = -1, -1
    remainders = set()
    counts = defaultdict(defaultdict)
    for a in A:
        n, result = factorization(a)
        remainders.add(n)
        counts[a] = result
        if min_2 == -1:
            min_2 = result[2]
        else:
            min_2 = min(min_2, result[2])
        
        if min_3 == -1:
            min_3 = result[3]
        else:
            min_3 = min(min_3, result[3])

    if len(remainders) != 1:
        print(-1)
    else:
        ans = 0
        for a in A:
            ans += counts[a][2] - min_2
            ans += counts[a][3] - min_3
        
        print(ans)



def factorization(n):
    result = defaultdict(int)
    for i in [2, 3]:
        while n % i == 0:
            n //= i
            result[i] += 1
    return n, result



if __name__ == "__main__":
    main()