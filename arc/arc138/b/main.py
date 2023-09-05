import sys
from collections import deque

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    A = deque(map(int, input().split()))

    reverse = False
    while A:
        if A[-1] == (0 if not reverse else 1):
            A.pop()
        elif A[0] == (0 if not reverse else 1):
            A.popleft()
            reverse = not reverse
        else:
            print("No")
            break
    else:
        print("Yes")


if __name__ == "__main__":
    main()
