import math

def main():
    K = int(input())

    k = K
    ans = 0
    for i in range(2, math.ceil(math.sqrt(K))+1):
        cnt = 0
        while k % i == 0:
            k //= i
            cnt += 1
        
        n = 0
        while cnt > 0:
            n += i
            x = n
            while x % i == 0:
                cnt -= 1
                x //= i
        ans = max(ans, n)

    ans = max(ans, k)
    print(ans)


if __name__ == "__main__":
    main()
