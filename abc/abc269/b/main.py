def main():
    S = [input() for _ in range(10)]
    
    A, B = 10, 0
    for i in range(10):
        s = S[i]
        if "#" in s:
            A = min(A, i + 1)
            B = max(B, i + 1)
            C = s.find("#") + 1
            D = s.rfind("#") + 1
            
    print(A, B)
    print(C, D)

if __name__ == "__main__":
    main()