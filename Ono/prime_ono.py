import sys
args = sys.argv
num = int(args[1])

#通常の処理
if num < 1000:
    for i in range(1,1000,1):
        if num % i == 0:
            print("Prime")
            break
    else:
        print("not")
#1000以上が入力された場合の処理
else:
    print("1000以上は判定できません")