import sys

# 引数入力
args = sys.argv
# 商品の値段（唐揚げ定食、カレーセット
price = (760, 850)
# 売上高
total_sales = 0
# 売上高計算
total_sales = price[0] * int(args[1]) + price[1] * int(args[2])
# 売上高表示
print(total_sales, end="")