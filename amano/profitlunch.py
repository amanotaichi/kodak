import sys

# 引数入力
args = sys.argv
# 例外処理
# 引数の数のチェック
if len(args)== 3:
    pass
else:
    print("引数エラー")
    sys.exit()

# 引数が整数かのチェック
for i in range(1, len(args)):
    if int(args[i]) < 0:
        print("正の整数を入力してください")
        sys.exit()
    else:
        pass

# 定数の設定
# 商品の値段（唐揚げ定食、カレーセット
price = [760, 850]
# 商品の原価率（唐揚げ定食、カレーセット
gross_profit = [0.323, 0.284]

# 変数の初期化
# 商品ごとの売上高
sales = [0, 0]
# 商品ごとの原価
gross_profit_sales = [0, 0]
# 合計売上高
total_sales = 0

# 関数
# 商品ごとの売上高計算
def calc_sales(price, num):
    return price * num
# 商品ごとの原価計算
def calc_gross_profit_sales(price, num, gross_profit):
    return int(round((price * num) * gross_profit))

# 計算
# 商品ごとの売上高計算
for i in range(len(price)):
    sales[i] = calc_sales(price[i], int(args[i + 1]))
# 売上高計算
for i in sales:
    total_sales += i
# 商品ごとの原価計算
for i in range(len(price)):
    gross_profit_sales[i] = calc_gross_profit_sales(price[i], int(args[i + 1]), gross_profit[i])

# 表示
print("売上高：" + str(total_sales) + "、", end="")
print("原価：" + str((gross_profit_sales[0] + gross_profit_sales[1])) + "、", end="")
print("粗利：" + str((total_sales - (gross_profit_sales[0] + gross_profit_sales[1]))), end="")