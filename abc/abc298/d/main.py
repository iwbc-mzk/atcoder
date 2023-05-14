from math import pow

MOD = 998244353

def main():
    Q = int(input())

    s = 1
    dn = 1
    for _ in range(Q):
        i, *j = input().split()
        if i == "1":
            j = j[0]
            s = 10 * s + int(j)
            dn += 1
        if i == "2":
            s %= int(pow(10, dn - 1))
            dn -= 1
        if i == "3":
            print(s % 998244353)


if __name__ == "__main__":
    main()
