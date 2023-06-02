import sys

input = sys.stdin.readline

def main(N, calls):
    """
    コードの説明
    """
    strike_counter = 0
    ball_counter = 0
    for i in calls:
        if i == "ball":
            print("ball!")
            ball_counter += 1
        elif i == "strike":
            print("strike!")
            strike_counter += 1
        
    if strike_counter == 3:
        print("out!")
    if ball_counter == 4:
        print("fourball!")



if __name__ == '__main__':
    # 入力を受け取る
    N = int(input())
    calls = [input().rstrip('\r\n') for _ in range(N)]

    # 出力
    main(N, calls)