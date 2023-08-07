from math import acos, sqrt, degrees


def main():
    A = tuple(map(int, input().split()))
    B = tuple(map(int, input().split()))
    C = tuple(map(int, input().split()))
    D = tuple(map(int, input().split()))

    def judge(v1, v2, a, b):
        if a[0] != b[0]:
            t = (a[1] - b[1]) / (a[0] - b[0])
            tt = a[1] - a[0] * t
            f = lambda x: t * x + tt
            if (v1[1] - f(v1[0])) * (v2[1] - f(v2[0])) >= 0:
                return False
        else:
            if (v1[0] - a[0]) * (v2[0] - a[0]) >= 0:
                return False

        return True

    if not judge(A, C, B, D):
        print("No")
        return

    if not judge(B, D, A, C):
        print("No")
        return

    print("Yes")


if __name__ == "__main__":
    main()
