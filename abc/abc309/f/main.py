def main():
    N = int(input())
    BOX = [sorted(list(map(int, input().split())), reverse=True) for _ in range(N)]
    BOX.sort(key=lambda x: max(x), reverse=True)

    for i in range(N):
        b1 = BOX[i]
        for j in range(i + 1, N):
            b2 = BOX[j]
            for k in range(3):
                if b1[k] <= b2[k]:
                    break
            else:
                print("Yes")
                return
    else:
        print("No")


if __name__ == "__main__":
    main()
