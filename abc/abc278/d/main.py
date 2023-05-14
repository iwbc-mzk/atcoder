from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    Q = int(input())

    a_all = None
    add_i = defaultdict(int)
    for _ in range(Q):
        q = list(map(int, input().split()))
        if q[0] == 1:
            a_all = q[1]
            add_i = defaultdict(int)
        if q[0] == 2:
            i, x = q[1]-1, q[2]
            add_i[i] += x
        if q[0] == 3:
            i = q[1] - 1
            if a_all:
                print(a_all + add_i[i])
            else:
                print(A[i] + add_i[i])


if __name__ == "__main__":
    main()