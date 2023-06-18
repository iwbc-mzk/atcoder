def main():
    N = int(input())
    P = list(map(int, input().split()))

    idxs = {}
    for i in range(N):
        idxs[P[i]] = i

    ans = []
    for num in range(1, N):
        i = idxs[num]
        if i == N - 1:
            break

        j = num - 1
        if i == j:
            continue

        ans.append((i, j))
        for key in idxs:
            if idxs[key] == i:
                idxs[key] = j
            elif idxs[key] == i + 1:
                idxs[key] = j + 1
            elif j <= idxs[key] <= i:
                idxs[key] += 2

    for k, v in idxs.items():
        if k != v + 1:
            print("No")
            return
    else:
        print("Yes")
        print(len(ans))
        for i, j in ans:
            print(i + 1, j)


if __name__ == "__main__":
    main()
