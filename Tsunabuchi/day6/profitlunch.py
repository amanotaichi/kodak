import sys
args = sys.argv
karaage_order = int(args[1])
curry_order = int(args[2])

# 唐揚げ定食の売上高
karaage_sales = 760 * karaage_order
# カレーセットの売上高
curry_sales = 850 * curry_order

# 唐揚げ定食の原価
karaage_prime_cost = round(karaage_sales * 0.323)
# カレーセットの原価
curry_prime_cost = round(curry_sales * 0.284)

# 唐揚げ定食の粗利
karaage_profit = karaage_sales - karaage_prime_cost
# カレーセットの粗利
curry_profit = curry_sales - curry_prime_cost

# 売上高の合計
sales = karaage_sales + curry_sales
# 原価の合計
prime_cost = karaage_prime_cost + curry_prime_cost
# 粗利の合計
profit = karaage_profit + curry_profit

print("売上高：" + str(sales) + "、原価：" + str(prime_cost) + "、粗利：" + str(profit),end="")