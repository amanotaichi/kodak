import sys
args = sys.argv

num = int(args[1])

# 1とnumでしか割れない

if num >= 1000 :
    print("1000以上は判定できません", end="")
elif num == 1:
    print("not", end="")
else:
    for i in range(2,num+1):       # iは2からnumまで
            #print(i)
            if num % i == 0:       # 割り切れたらループを抜ける
                break
    if i == num:                   # numが7なら7÷7で割り切れるから
        print("Prime", end="")
    else:
        print("not", end="")


