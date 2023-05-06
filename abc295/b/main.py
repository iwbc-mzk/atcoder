import math

def main():
    R, C = map(int, input().split())
    B = [list(input()) for _ in range(R)]

    l = []
    for i in range(0, R):
        for j in range(0, C):
            l.append((i, j))

    bo = set()
    for l1 in l:
        for l2 in l:
            ar, ac = l1
            br, bc = l2

            a = B[ar][ac]
            if a.isdecimal():
                bo.add(l1)
                if ar == br and ac == bc or B[br][bc].isdecimal():
                    continue
                d = abs(ar - br) + abs(ac - bc)
                if d <= int(a):
                    B[br][bc] = "."

    for r, c in bo:
        B[r][c] = "."

    for i in B:
        print("".join(i))
        
            


if __name__ == "__main__":
    main()