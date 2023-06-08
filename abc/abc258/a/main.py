def main():
    K = int(input())
    h = 21 + K // 60
    m = 0 + K % 60


    print(f"{h}:{str(m).zfill(2)}")


if __name__ == "__main__":
    main()
