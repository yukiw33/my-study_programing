import sys
import collections

input = sys.stdin.readline

# 1行空白ありの文字列入力を、空白区切りのリストとして受け取る
words = input().split()

# 受け取った入力を辞書型にして出現回数もカウントする
c = collections.Counter(words)

# 辞書型をkeyとvalueどちらも1つずつ出力
for k, v in c.items():
    print(k, v)
