from collections import defaultdict, deque


def main():
    N = int(input())
    A = list(map(int, input().split()))

    L = defaultdict(deque)
    R = defaultdict(deque)
    for i, a in enumerate(A):
        R[a].append(i)

    ans = 0
    pre = 0
    for i in range(N):
        if i == 0:
            continue

        pa, a = A[i - 1], A[i]
        if pa == a:
            ans += pre
            L[a].append(R[pa].popleft())
            continue

        pre -= len(L[a]) * len(R[a])
        L[pa].append(R[pa].popleft())
        pre += len(L[pa]) * len(R[pa])
        ans += pre

    print(ans)


if __name__ == "__main__":
    main()
