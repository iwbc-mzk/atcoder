from queue import Queue
from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    gragh = defaultdict(set)
    for i in range(N // 2 + 1):
        a1, a2 = A[i], A[N - 1 - i]
        gragh[a1].add(a2)
        gragh[a2].add(a1)

    visited = set()
    ans = 0
    for i in set(A):
        cnt = 0
        q = Queue()
        if i not in visited:
            q.put(i)
            visited.add(i)
            cnt += 1

        while not q.empty():
            v = q.get()
            for vv in gragh[v]:
                if vv not in visited:
                    q.put(vv)
                    visited.add(vv)
                    cnt += 1
        else:
            if cnt:
                ans += cnt - 1

    print(ans)


if __name__ == "__main__":
    main()
