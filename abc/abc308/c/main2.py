from functools import cmp_to_key


def cmp(a, b):
    v1 = a[0] * b[1]
    v2 = a[1] * b[0]
    if v1 == v2:
        if a[2] == b[2]:
            return 0
        elif a[2] < b[2]:
            return 1
        else:
            return -1
    elif v1 < v2:
        return -1
    else:
        return 1


def main():
    N = int(input())

    suc = []
    for i in range(N):
        a, b = map(int, input().split())
        suc.append((a, b, i + 1))

    suc.sort(key=cmp_to_key(cmp), reverse=True)
    ans = []
    for a in suc:
        ans.append(a[2])

    print(*ans)


if __name__ == "__main__":
    main()
