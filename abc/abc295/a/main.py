def main():
    N = int(input())
    W = input().split()
    for w in W:
        if w in ["and", "not", "that", "the", "you"]:
            print("Yes")
            break
    else:
        print("No")


if __name__ == "__main__":
    main()