def main():
    N, K = map(int, input().split())
    R, S, P = map(int, input().split())
    T = input()

    hist = []
    ans = 0
    for i, t in enumerate(T, 1):
        idx = i - 1
        if i <= K:
            if t == "r":
                ans += P
                hist.append("p")
            if t == "s":
                ans += R
                hist.append("r")
            if t == "p":
                ans += S
                hist.append("s")
        else:
            if t == "r" and hist[idx - K] != "p":
                ans += P
                hist.append("p")
            elif t == "s" and hist[idx - K] != "r":
                ans += R
                hist.append("r")
            elif t == "p" and hist[idx - K] != "s":
                ans += S
                hist.append("s")
            else:
                hist.append("-")
    
    print(ans)


if __name__ == "__main__":
    main()