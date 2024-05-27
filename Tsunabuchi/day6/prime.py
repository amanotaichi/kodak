import sys
args = sys.argv
num = int(args[1])

if num >= 1000:
    print("1000以上は判定できません",end="")

elif num < 2:
    print("not",end="")

elif 2 <= num < 1000:
    for i in range(2, num):
        if num % i == 0:
            print("not",end="")
            break
        else:
            pass

    else:
        print("Prime",end="") 
