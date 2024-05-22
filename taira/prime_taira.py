import sys
args =  sys.argv

input = int(args[1])

if input >=1000 :
    print("1000以上は判定できません")
elif input == 1:
    print("prime")
else:
    for i in range(2,input+1):
        a = input % i
        if a == 0: break
        
    if i == input :
        print("prime")
    else:
        print("not")

