import math

def main():
    A, B = map(int, input().split())

    t = (A / (2 * B)) ** (2 / 3) - 1
    start = math.ceil(t - 5) if math.ceil(t - 5) > 0 else 0
    end = math.ceil(t + 5)
    ans = None
    for i in range(start, end):
        v = B * (i) + A / math.sqrt(1+i)
        if ans is None:
            ans = v
        else:
            ans = min(ans, v)


    print(ans)



if __name__ == "__main__":
    main()