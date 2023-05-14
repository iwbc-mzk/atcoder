import math
from collections import defaultdict

CACHE = defaultdict(float)
def f(n: int) -> float:
    if n == 0:
        return 1
    
    if n in CACHE:
        return CACHE[n]
    
    result = f(math.floor(n/2)) + f(math.floor(n/3))
    CACHE[n] = result
    return result

def main():
    N = int(input())
    print(f(N))


if __name__ == "__main__":
    main()