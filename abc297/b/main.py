import re

def main():
    S = input()

    b = [m.start() for m in re.finditer("B", S)]
    r = [m.start() for m in re.finditer("R", S)]
    k = [m.start() for m in re.finditer("K", S)]

    ans = True
    if b[0] % 2 == b[1] % 2:
        ans = False

    if r[0] > k[0] or k[0] > r[1]:
        ans = False

    print("Yes" if ans else "No")



if __name__ == "__main__":
    main()