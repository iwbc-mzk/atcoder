def swap(indexes, i, j):
    i -= 1
    num, next_num = None, None
    for k in indexes:
        if indexes[k] == i:
            num = k

        if indexes[k] == i + 1:
            next_num = k

        if j <= indexes[k] < i:
            indexes[k] += 2

    indexes[num] = j
    indexes[next_num] = j + 1


def main():
    N = int(input())
    P = list(map(int, input().split()))

    indexes = {}
    ans = []
    for i in range(N):
        indexes[P[i]] = i

    for i in range(N - 1):
        num = i + 1
        if indexes[num] == i:
            continue
        else:
            num_idx = indexes[num]
            if num_idx == N - 1:
                swap(indexes, N - 1, N - 3)
                ans.append((N - 1, N - 3))
                num_idx = indexes[num]
            swap(indexes, num_idx + 1, i)
            ans.append((num_idx + 1, i))

    for k, v in indexes.items():
        if k != v + 1:
            print("No")
            return

    print("Yes")
    print(len(ans))
    for a in ans:
        print(*a)


if __name__ == "__main__":
    main()
