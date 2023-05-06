def main():
    N, K = map(int, input().split())
    A = input().split()

    for _ in range(K):
        A.pop(0)
        A.append("0")
    
    print(" ".join(A))


if __name__ == "__main__":
    main()