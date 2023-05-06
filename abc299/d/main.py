def main():
    N = int(input())
    begin = 0
    end = N

    for i in range(21):
        idx = (begin + end) // 2
        print(f"? {idx}")
        ans = int(input())
        if ans == 0:
            begin = idx
        else:
            end = idx
        
        if end - begin <= 1:
            print(f"! {begin}")
            break


if __name__ == "__main__":
    main()