list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
oddlist = []
for i in range(0,8,1):
    if i % 2 != 0:
        oddlist.append(list[i])

print(oddlist)