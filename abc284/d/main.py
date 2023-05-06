import math

def is_prime(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i:
            return False
    return True        


def main():
    T = int(input())

    prime = [2, 3, 5]
    for _ in range(T):
        N = int(input())

        p, q = None, None
        for i in prime:
            if N % i**2 == 0:
                p = i
                q = N // p**2
                break
            elif N % i == 0:
                q = i
                p = int(math.sqrt(N//q))
                break
        
        if not p and not q:
            max_prime = prime[-1]
            for i in range(max_prime+1, N+1):
                if is_prime(i):
                    continue
                else:
                    prime.append(i)

                if N % i**2 == 0:
                    p = i
                    q = N // p**2
                    break
                elif N % i == 0:
                    q = i
                    p = int(math.sqrt(N//q))
                    break
        
        print(f"{p} {q}")

            
            


if __name__ == "__main__":
    main()