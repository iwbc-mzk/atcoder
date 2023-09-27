import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    XYH = [tuple(map(int, input().split())) for _ in range(N)]
    XYH.sort(key=lambda x: x[2], reverse=True)

    for cx in range(101):
        for cy in range(101):
            H = None
            for x, y, h in XYH:
                if H is None:
                    if h != 0:
                        H = abs(x - cx) + abs(y - cy) + h
                else:
                    if h != max(H - abs(x - cx) - abs(y - cy), 0):
                        break
            else:
                print(cx, cy, H)
                return


if __name__ == "__main__":
    main()
