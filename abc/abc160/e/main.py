from collections import deque


def main():
    X, Y, A, B, C = map(int, input().split())
    PA = list(map(int, input().split()))
    QB = list(map(int, input().split()))
    RC = list(map(int, input().split()))

    PA.sort()
    pa = deque(PA[-X:])
    QB.sort()
    qb = deque(QB[-Y:])
    RC.sort()
    rc = deque(RC)

    for _ in range(C):
        c = rc.pop()
        if pa[0] <= qb[0] and pa[0] < c:
            pa.popleft()
            pa.append(c)
        elif pa[0] > qb[0] and qb[0] < c:
            qb.popleft()
            qb.append(c)
        else:
            break

    print(sum(pa) + sum(qb))


if __name__ == "__main__":
    main()
