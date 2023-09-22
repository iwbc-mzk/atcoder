# 約数列挙
# 計算量O(√N)
# 参考: https://qiita.com/LorseKudos/items/9eb560494862c8b4eb56
def enumerate_divisors(n):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n // i)
        i += 1
    return lower_divisors + upper_divisors[::-1]
