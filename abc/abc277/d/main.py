def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    
    count = {}
    total = 0
    for a in A:
        total += a
        if a not in count:
            count[a] = 0
        count[a] += 1

    if len(count.keys()) == M:
        print(0)
        return

    ans = total
    visited = set()
    for start in count.keys():
        if start in visited:
            continue

        prev = (start - 1) % M
        if prev not in visited and prev in count:
            continue

        next_key = start
        visited.add(start)
        m = 0
        while next_key >= 0:
            m += count[next_key] * next_key

            next_key = (next_key + 1) % M
            if next_key not in count or next_key in visited:
                next_key = -1
                break
        
        ans = min(ans, total - m)
                
    print(ans)


if __name__ == "__main__":
    main()