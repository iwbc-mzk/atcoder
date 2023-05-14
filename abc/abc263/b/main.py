from queue import Queue

def main():
    N = int(input())
    P = list(map(int, input().split()))

    d = {}
    for i, p in enumerate(P, 2):
        d[i] = p

    q = Queue()
    q.put(N)
    ans = 0
    while not q.empty():
        v = q.get()
        if v != 1:
            q.put(d[v])
            ans += 1

    print(ans)



if __name__ == "__main__":
    main()