from collections import deque


def main():
    L, N1, N2 = map(int, input().split())

    A1 = deque(tuple(map(int, input().split())) for _ in range(N1))
    A2 = deque(tuple(map(int, input().split())) for _ in range(N2))

    ans = 0
    v1, l1 = A1.popleft()
    v2, l2 = A2.popleft()
    i = 0
    i1, i2 = l1, l2
    while True:
        l = min(i1, i2)
        if v1 == v2:
            ans += l - i

        i = l
        if i == i1:
            if not A1:
                break
            v1, l1 = A1.popleft()
            i1 = l + l1

        if i == i2:
            if not A2:
                break
            v2, l2 = A2.popleft()
            i2 = l + l2

    print(ans)


if __name__ == "__main__":
    main()
