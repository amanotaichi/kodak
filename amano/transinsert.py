import sys
from databases import session
from tables import Transport

# 引数入力
args = sys.argv

# 関数
# データベース登録
# 登録データの編集
def insert_data(args):
    trancedata = Transport(
        date = args[1],
        seq = args[2],
        departure = args[3],
        arrival = args[4],
        via = args[5],
        amount = args[6]
    )

    # insert処理
    session.add(trancedata)

    # commit処理
    session.commit()

    # 結果表示
    print("登録しました")
    return

try:
    insert_data(args)
except:
    # 結果表示
    print("error:登録できませんでした")