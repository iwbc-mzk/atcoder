from collections import Counter, defaultdict

def main():
    S = input()

    ans = 0
    for l in range(len(S)):
        d = defaultdict(int)
        pre = 0
        for r in range(l+2, len(S)+1, 2):
            if (r - l) % 2:
                continue

            while pre < r:
                d[S[pre]] += 1
                pre += 1

            # c = Counter(list(S[l:r]))
            if len(d):
                for v in d.values():
                    if v % 2:
                        break
                else:
                    ans += 1
                    

    print(ans)


if __name__ == "__main__":
    main()