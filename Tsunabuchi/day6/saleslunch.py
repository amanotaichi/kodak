import sys
args = sys.argv
karaage_order = int(args[1])
curry_order = int(args[2])

sales = (760 * karaage_order) + (850 * curry_order)

print(sales,end="")