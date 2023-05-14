def main():
    N = int(input())
    S = list(input())
    
    t = 0
    a = 0
    for s in S:
        if s == "T":
            t += 1
        else:
            a += 1
        if t > a and t >= N // 2:
            print("T")
            break
        if a > t and a >= N // 2:
            print("A")
            break
    
    


if __name__ == "__main__":
    main()