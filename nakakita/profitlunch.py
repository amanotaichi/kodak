import sys
args = sys.argv

from decimal import Decimal, ROUND_HALF_UP

karaage = int(args[1])
curry = int(args[2])

#売上高
karaage_sales = karaage * 760
curry_sales = curry * 850
sales = karaage_sales + curry_sales


#原価
karaage_cost = karaage_sales * 0.323
curry_cost = curry_sales * 0.284

karaage_cost =Decimal(str(karaage_cost)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)
curry_cost =Decimal(str(curry_cost)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

cost = karaage_cost + curry_cost

#売上
income = sales - cost

print("売上高：" + str(sales) + "、原価：" + str(cost) + "、粗利：" + str(income), end="")