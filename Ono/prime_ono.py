import sys
args = sys.argv
num = int(args[1])

#通常の処理
if num == 1 or num == 2:
    print("Prime")

elif 2 < num < 1000:
    for i in range(2, num - 1, 1):
        if num % i == 0:
            print("not")
            break
        else:
            pass
    else:
        print("Prime")

#1000以上が入力された場合の処理
else:
    print("1000以上は判定できません")