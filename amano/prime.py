import sys

# 引数の入力
args = sys.argv

# 入力チェック
if len(args) != 2:
    print("引数エラー", end="")
    sys.exit()
elif int(args[1]) >= 1000:
    print("1000以上は判定できません", end="")
    sys.exit()
elif int(args[1]) < 0:
    print("負の整数が入力されました。正の整数を入力してください", end="")
    sys.exit()
else:
    pass

# 変数の初期化
num = int(args[1])
prime_count = 0

# 素数の判定
for i in range(2, num):
    print("for in")
    if num % i == 0:
        prime_count += 1
        break
    else:
        pass

# 結果出力
if prime_count == 0:
    print("Prime", end="")
else:
    print("not", end="")