import sys

# 引数入力
args = sys.argv
# 絶対値変換
# 表示
print(args[1] + " ", end="")
print(abs(int(args[1])), end="")