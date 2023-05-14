from collections import defaultdict

def main():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))

    times = defaultdict(int)
    times[0] = 0
    for i, a in enumerate(A):
        if i == 0:
            times[i+1] = a
        else:
            times[i+1] = times[i] + a

    remainder = T % times[len(A)]
    for i, a in times.items():
        if a < remainder < a + A[i]:
            print(i+1, remainder - a)


if __name__ == "__main__":
    main()