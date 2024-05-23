import sys
args = sys.argv

distance = int(args[1])

if distance <= 1500:
    price = 630
elif distance > 1500:
    if (distance - 1500) % 344 == 0:
        price = 630 + ((distance - 1500) / 344) * 98
    else:
        price = 630 + 98 + ((distance - 1500) // 344) * 98

print(price, end="")