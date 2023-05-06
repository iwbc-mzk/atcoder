def main():
    K = int(input())
    
    result = ""
    for i in range(K):
        result += chr(ord("A") + i).upper()

    print(result)


if __name__ == "__main__":
    main()