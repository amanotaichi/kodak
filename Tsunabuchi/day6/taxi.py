import sys
args = sys.argv
distance = int(args[1])

fare = 0

if distance <= 1500:
    fare = 630

elif distance > 1500 :
    if (distance-1500) / 344 == 0:
        fare = (distance-1500) / 344 * 98 + 630
    else:
        fare = ((distance-1500) // 344) * 98 + 98 + 630

print(fare,end="")