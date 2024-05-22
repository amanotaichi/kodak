import sys
args = sys.argv
karaage = int(args[1])
curry = int(args[2])

#売上高の計算
sales = karaage * 760 + curry * 850
#原価の計算
prime_cost = int(round((karaage * 760) * 0.323)) + int(round((curry * 850) * 0.284))
#粗利の計算
gross_profit = sales - prime_cost

print("売上高：" + str(sales) + "、原価：" + str(prime_cost) + "、粗利：" + str(gross_profit))