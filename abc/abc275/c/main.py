from itertools import combinations

def main():
    P = set()
    for i in range(9):
        s = list(input())
        for j, si in enumerate(s):
            if si == "#":
                P.add((i, j))

    comb = combinations(P, 4)
    cnt = 0
    for a, b, c, d in comb:
        for p1, p2, p3, p4 in [(a, b, c, d), (a, c, b, d), (a, d, b, c)]:
            # 対角線が直交しているか
            if (p1[0] - p2[0]) * (p3[0] - p4[0]) + (p1[1] - p2[1]) * (p3[1] - p4[1]) != 0:
                continue

            d12 = (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
            d34 = (p3[0] - p4[0]) ** 2 + (p3[1] - p4[1]) ** 2
            # 対角線の長さが等しいか
            if d12 != d34:
                continue

            # 対角線が互いの中点で交わっているか
            c12 = ((p1[0] + p2[0])/2, (p1[1] + p2[1])/2)
            c34 = ((p3[0] + p4[0])/2, (p3[1] + p4[1])/2)
            if c12 != c34:
                continue
                    
            cnt += 1
            break
    
    print(cnt)

if __name__ == "__main__":
    main()
