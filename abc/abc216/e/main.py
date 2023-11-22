import sys
import heapq

sys.setrecursionlimit(10**9)


def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    AA = [-a for a in A]
    heapq.heapify(AA)

    ans = 0
    now = -heapq.heappop(AA)
    c = 1
    while K > 0:
        nv = now
        while True and AA:
            nv = -heapq.heappop(AA)
            if now != nv:
                break
            else:
                c += 1

        if K >= (now - nv) * c and now != nv:
            ans += (now + (nv + 1)) * (now - nv) // 2 * c
            K -= (now - nv) * c
            c += 1
            now = nv
        else:
            l, r = -1, now
            while r - l > 1:
                m = (l + r) // 2
                if K <= (now - m) * c:
                    l = m
                else:
                    r = m

            ans += (now + (r + 1)) * (now - r) // 2 * c
            K -= (now - r) * c
            now = r
            ans += r * K
            K = 0

    print(ans)


if __name__ == "__main__":
    main()
