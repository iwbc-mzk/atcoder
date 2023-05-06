import math

def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False

    return prime


def main():
    N = int(input())

    prime_bool = sieve_of_eratosthenes(math.ceil(math.sqrt(N / 12)) + 1)
    prime_list = []
    for p in range(math.ceil(math.sqrt(N/ 12)) + 1):
        if prime_bool[p]:
            prime_list.append(p)

    ans = 0
    for i in range(len(prime_list) - 2):
        if prime_list[i] **2 * prime_list[i + 1] * prime_list[i + 2] ** 2 > N:
                break
        
        k = len(prime_list) - 1
        for j in range(i + 1, len(prime_list) - 1):
            if prime_list[i] **2 * prime_list[j] * prime_list[j + 1] ** 2 > N:
                break

            l = N / (prime_list[i] **2 * prime_list[j])
            while j < k:
                if prime_list[k] ** 2 > l:
                    k -= 1
                else:
                    break
            
            if j < k:
                ans += k - j
    
    print(ans)

if __name__ == "__main__":
    main()