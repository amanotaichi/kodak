import sys
import math

# 引数入力
args = sys.argv
# 走行距離を変数に代入
distance = abs(int(args[1]))
# 走行処理と料金
mile = (1500, 344)
price = (630, 98)
# 合計金額
total_price = 0
# 運賃計算
if distance <= mile[0]:
    total_price = price[0]
elif distance > mile[0]:
    # total_price = price[0] + (math.ceil((distance - mile[0]) / mile[1])) * price[1]
    total_price = price[0] + math.ceil((distance - mile[0]) / mile[1]) * price[1]
else:
    pass

print(total_price, end="")