import sys

input = sys.stdin.readline

def main(H, W, N, cards, L, moves):
    """
    """
    counts = [0]*N
    turn = 0

    for move in moves:
        a, b, A, B = move
        if cards[a-1][b-1] == cards[A-1][B-1]:
            counts[turn] += 2
            cards[a-1][b-1] = cards[A-1][B-1] = 0
        else:
            turn = (turn + 1) % N
    
    for count in counts:
        print(count)

if __name__ == '__main__':
    # 入力を受け取る
    H, W, N = map(int, input().split())
    cards = [list(map(int, input().split())) for _ in range(H)]
    L = int(input())
    moves = [list(map(int, input().split())) for _ in range(L)]

    # 出力
    main(H, W, N, cards, L, moves)