import sys
from databases import session
from tables import Lunch

# 引数入力
args = sys.argv

# データベース全取得
lunchlist = session.query(Lunch).all()

# 処理の選択
# 商品の粗利計算
if args[1].isdigit():
    pass
# データベースに商品追加
elif args[1] == "insert":
    lunch = Lunch(
        seq = len(lunchlist) + 1,
        name = args[2],
        price = int(args[3]),
        cost = float(args[4])
    )
    session.add(lunch)
    session.commit()
    sys.exit()
# データベースから商品削除
elif args[1] == "delete":
    lunch = session.query(Lunch).filter(Lunch.seq == int(args[2])).first()
    session.delete(lunch)
    session.commit()
    sys.exit()
# データベース表示
elif args[1] == "show":
    for lunch in lunchlist:
        print(lunch.seq, lunch.name, lunch.price, lunch.cost)
    sys.exit()
elif args[1] == "help":
    print(
        "コマンドリスト\n"+
        "商品の粗利計算：商品の売上個数を入力\n"+
        "商品をデータベースに追加：insert 商品名 原価 原価率\n"+
        "商品をデータベースから削除：delete 商品番号\n"+
        "商品リストを表示：show\n"+
        "コマンドヘルプ：help"
    )
    sys.exit()
# 未指定の処理宣言
else:
    print("引数エラー")
    sys.exit()

# 商品リスト表示
print("商品リスト")
for lunch in lunchlist:
    print(lunch.seq, lunch.name, lunch.price, lunch.cost)
print("-----")

# 例外処理
# 引数の数のチェック
if len(args)== len(lunchlist) + 1:
    pass
else:
    print("引数の数エラー")
    sys.exit()

# 引数が整数かのチェック
for i in range(1, len(args)):
    if int(args[i]) < 0:
        print("正の整数を入力してください")
        sys.exit()
    else:
        pass

# 変数の初期化
# 商品ごとの売上高
sales = [0] * 10
# 商品ごとの原価
gross_profit_sales = [0] * 10
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
# 商品ごとの売上額、合計金額、粗利の算出
for i in range(len(lunchlist)):
    sales[i] = calc_sales(lunchlist[i].price, int(args[i + 1]))
    total_sales += sales[i]
    gross_profit_sales[i] = calc_gross_profit_sales(lunchlist[i].price, int(args[i + 1]), lunchlist[i].cost)

# 結果表示
# 商品リストと売上個数
print("売上商品数")
for i in range(len(lunchlist)):
    print(lunchlist[i].name + "：" + str(args[i+1]) + "個")
# 計算結果表示
print("売上高：" + str(total_sales) + "、", end="")
print("原価：" + str((gross_profit_sales[0] + gross_profit_sales[1])) + "、", end="")
print("粗利：" + str((total_sales - (gross_profit_sales[0] + gross_profit_sales[1]))))
