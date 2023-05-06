def main():
    N = int(input())
    S = list(input())

    for i in range(1, N):
        for l in reversed(range(N-i+1)):
            for k in range(1, l+1):
                if S[k-1] == S[k+i-1]:
                    break
            else:
                print(l)
                break



if __name__ == "__main__":
    main()