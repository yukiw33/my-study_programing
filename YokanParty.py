import sys
input = sys.stdin.readline

def check(x,N,A,L,K):
    # 判定問題 全ての長さがx以上か？
    num = 0 # 何個切れたか
    pre = 0 # 前回の切れ目
    for i in range(N):
        # x を超えたら切断する
        if A[i] - pre >= x:
            num += 1
            pre = A[i]
    # 最後のピースが x 以上なら加算する
    if L - pre >= x:
        num += 1
    return (num >= K + 1)

def main(N,A,L,K):
    # 2分探索プログラム
    left, right = -1, L + 1
    while right - left > 1:
        mid = (left + right) // 2
        if check(mid,N,A,L,K):
            left = mid
        else:
            right = mid
    print(left)



if __name__ == '__main__':
    # 入力を受け取る
    N, L = map(int, input().strip().split())
    K = int(input())
    A = list(map(int, input().split()))
    main(N,A,L,K)