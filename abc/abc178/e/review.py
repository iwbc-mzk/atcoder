def main():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    rot_X, rot_Y = [], []
    for x, y in XY:
        rot_X.append(x + y)
        rot_Y.append(x - y)

    rot_X.sort()
    rot_Y.sort()

    ans = max(rot_X[-1] - rot_X[0], rot_Y[-1] - rot_Y[0])
    print(ans)


if __name__ == "__main__":
    main()
