def main():
    N = int(input())
    s = input()

    q = []
    cnt = 0
    for i, si in enumerate(s):
        q.append(si)
        if i >= 2 and q[-3:] == ["f", "o", "x"]:
            cnt += 1
            for _ in range(3):
                q.pop()

    ans = len(q)
    print(ans)


if __name__ == "__main__":
    main()
