from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    G = defaultdict(set)

    A = list(map(int, input().split()))
    for i, a in enumerate(A, 1):
        G[i].add(a)

    finished = set()
    for i in range(1, N + 1):
        if i in finished:
            continue

        finished.add(i)
        root = deque()
        root.append(i)

        visited = set()
        ans = []

        def rec(v):
            root.append(v)
            finished.add(v)

            for vv in G[v]:
                if vv not in visited:
                    visited.add(vv)
                    rec(vv)
                else:
                    flg = False
                    for r in root:
                        if r == vv:
                            flg = True

                        if flg:
                            ans.append(r)
            root.pop()

        rec(i)

        if ans:
            print(len(ans))
            print(*ans)
            return


if __name__ == "__main__":
    main()
