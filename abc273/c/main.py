from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))

    value_to_idx = defaultdict(set)
    for i, a in enumerate(A):
        value_to_idx[a].add(i)

    cnt_dict = defaultdict(int)
    a_sorted = sorted(set(A))
    for i in range(len(a_sorted)):
        if i == len(a_sorted) - 1:
            cnt_dict[0] = a_sorted[i]
            break

        if a_sorted[i] != a_sorted[i + 1]:
            cnt_dict[len(a_sorted) - (i + 1)] = a_sorted[i]

    for i in range(N):
        print(len(value_to_idx[cnt_dict[i]]))



if __name__ == "__main__":
    main()