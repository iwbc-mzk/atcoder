def main():
    S = input()

    ans = 0
    for s in list(S):
        if s == "v":
            ans += 1
        
        if s == "w":
            ans += 2
    
    print(ans)


if __name__ == "__main__":
    main()