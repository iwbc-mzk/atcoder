def main():
    K = int(input())

    if K % 2 == 0:
        print(-1)
    else:
        i = 7
        for j in range(K):
            if i % K == 0:
                print(j + 1)
                return
            i *= 10
            i += 7
            i %= K
        else:
            print(-1)


if __name__ == "__main__":
    main()
