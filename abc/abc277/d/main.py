from collections import defaultdict

def main():
    with open(r"C:\Users\iwbc_\PycharmProjects\Sandbox\atcoder\abc277\d\tests\005.in", "r") as f:
        N, M = map(int, f.readline().split())
        A = list(map(int, f.readline().split()))

    # N, M = map(int, input().split())
    # A = list(map(int, input().split()))

    d = defaultdict(int)
    a_sum = 0
    keys = set()
    for a in A:
        d[a] += a
        a_sum += a
        keys.add(a)

    ans = a_sum
    cache = defaultdict(int)
    # keys = set(d.keys())
    for start in keys:
        s = 0
        next_key = start
        while d[next_key]:
        # while next_key in keys:
            if cache[next_key]:
                s += cache[next_key]
                break

            s += d[next_key]
            next_key = (next_key + 1) % M

        cache[start] = s
        ans = min(ans, a_sum - s)
        if ans == 0:
            pass

    print(ans)


if __name__ == "__main__":
    main()