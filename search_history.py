import sys
import collections

input = sys.stdin.readline

# 入力を受け取る
N = int(input())
# 改行区切りの複数行の文字列をリストに入力, 改行を削除
history = [input().rstrip() for _ in range(N)]

# リストを逆順にする
history = history[::-1]

# リストから重複した要素を出現順の逆順に保持する
c = collections.Counter(history)

for k in c.keys():
    print(k)