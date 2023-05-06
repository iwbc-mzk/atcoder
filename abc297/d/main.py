def main():
    A, B = map(int, input().split())
    
    a, b = A, B
    ans = 0
    while a != b:
        if a > b:
            t = a // b
            if a % b == 0:
                t -= 1
            ans += t
            a -= b * t
        else:
            t = b // a
            if b % a == 0:
                t -= 1
            ans += t
            b -= a * t

    print(ans)

if __name__ == "__main__":
    main()