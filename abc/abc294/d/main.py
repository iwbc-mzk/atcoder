import heapq
from queue import Queue

def main():
    N, Q = map(int, input().split())

    not_called = Queue()
    for i in range(1, N+1):
        not_called.put(i)
    called = []
    visited_flg = [False] * N

    for _ in range(Q):
        event = list(map(int, input().split()))

        if event[0] == 1:
            h = not_called.get()
            heapq.heappush(called, h)
        elif event[0] == 2:
            h = event[1]
            visited_flg[h-1] = True
        elif event[0] == 3:
            h = None
            while not h and called:
                m = heapq.heappop(called)
                if not visited_flg[m-1]:
                    h = m
                    heapq.heappush(called, h)
            print(h)


if __name__ == "__main__":
    main()