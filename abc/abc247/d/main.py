from collections import deque


def main():
    Q = int(input())

    q = deque()
    for _ in range(Q):
        i, *xc = map(int, input().split())

        if i == 1:
            x, c = xc
            q.append((x, c))
        else:
            c = xc[0]
            ans = 0
            while c:
                x, xc = q.popleft()
                if xc <= c:
                    ans += x * xc
                    c -= xc
                else:
                    ans += x * c
                    q.appendleft((x, xc - c))
                    c = 0

            print(ans)


if __name__ == "__main__":
    main()
