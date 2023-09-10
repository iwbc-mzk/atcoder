def main():
    N = int(input())

    ans = []
    for i in range(N + 1):
        for j in range(1, 10):
            if i % (N / j) == 0:
                ans.append(str(j))
                break
        else:
            ans.append("-")

    print("".join(ans))


if __name__ == "__main__":
    main()
