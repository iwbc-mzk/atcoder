import sys

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())

    L = [-1] * N

    for i in range(1, N + 1, 3):
        print(f"? {i} {i + 1} {i + 2}")
        ans1 = int(input())
        if ans1 == -1:
            return

        print(f"? {i} {i + 1}")
        ans2 = int(input())
        if ans2 == -1:
            return

        print(f"? {i + 1} {i + 2}")
        ans3 = int(input())
        if ans3 == -1:
            return

        if ans1 == 0:
            if ans2 == 0:
                if ans3 == 0:
                    L[i] = 0
                    L[i + 1] = 0
                    L[i + 2] = 0
                else:
                    L[i] = 1
                    L[i + 1] = 1
                    L[i + 2] = 0
            else:
                if ans3 == 0:
                    print(f"? {i + 1}")
                    ans4 = int(input())
                    if ans4 == -1:
                        return
                    if ans4 == 0:
                        L[i] = 1
                        L[i + 1] = 0
                        L[i + 2] = 0
                    else:
                        L[i] = 0
                        L[i + 1] = 1
                        L[i + 2] = 1
                else:
                    print(f"? {i + 1}")
                    ans4 = int(input())
                    if ans4 == -1:
                        return
                    if ans4 == 0:
                        L[i] = 1
                        L[i + 1] = 0
                        L[i + 2] = 1
                    else:
                        L[i] = 0
                        L[i + 1] = 1
                        L[i + 2] = 0
        else:
            if ans2 == 0:
                if ans3 == 0:
                    L[i] = 1
                    L[i + 1] = 1
                    L[i + 2] = 1
                else:
                    print(f"? {i + 1}")
                    ans4 = int(input())
                    if ans4 == -1:
                        return
                    if ans4 == 0:
                        L[i] = 0
                        L[i + 1] = 0
                        L[i + 2] = 1
                    else:
                        L[i] = 1
                        L[i + 1] = 1
                        L[i + 2] = 0
            else:
                if ans3 == 0:
                    L[i] = 1
                    L[i + 1] = 0
                    L[i + 2] = 0
                else:
                    L[i] = 0
                    L[i + 1] = 1
                    L[i + 2] = 0

    print("!", *L)


if __name__ == "__main__":
    main()
