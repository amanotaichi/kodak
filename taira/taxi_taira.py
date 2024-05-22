import sys 
args=sys.argv

input = int(args[1])
hatsu = int(input) - 1500
if hatsu < 0:
    sum = 630
    print(sum)
elif hatsu % 344 == 0 :
    sum = 630 + (hatsu//344)*98
    print(sum)
elif hatsu % 344 !=0:
    sum = 630 + ((hatsu//344)+1)*98
    print(sum)
    


