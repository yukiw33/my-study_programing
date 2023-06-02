import sys

input = sys.stdin.readline

def main(n, k, visitor_sum):
    """
    コードの説明
    """
    max_visitors = 0
    start_promotion_date = 0
    counter = 0
    for i in range(n-k+1):
        s = sum(visitor_sum[i:i+k])
        if max_visitors < s:
            counter = 1
            max_visitors = s
            start_promotion_date = i + 1
        elif max_visitors == s:
            counter += 1

    print(counter, start_promotion_date)
        

    

if __name__ == '__main__':
    # 入力を受け取る
    n, k = map(int, input().split())
    visitor_sum = list(map(int, input().split()))
    
    # 出力
    main(n, k, visitor_sum)