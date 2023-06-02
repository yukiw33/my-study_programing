import sys

input = sys.stdin.readline

def main(b, N, my_lottery):
    """
    コードの説明
    """
    for i in my_lottery:
        if i == b:
            print("first")
        elif i == b-1 or i == b+1:
            print("adjacent")
        elif i % 10000 == b % 10000:
            print("second")
        elif i % 1000 == b % 1000:
            print("third")
        else:
            print("blank")


if __name__ == '__main__':
    # 入力を受け取る
    b = int(input())
    N = int(input())
    my_lottery = [int(input()) for _ in range(N)]

    # 出力
    main(b, N, my_lottery)
