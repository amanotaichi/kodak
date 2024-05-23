import sys
from databases import session
from tables import Transport

# 引数入力
args = sys.argv
# 出力ファイル名
filename = args[1]

# データベース全取得
transportlist = session.query(Transport).all()

# ファイルオープン
file = open(filename, "w")
# ファイルに追記
# file.write(transportlist.date)

# with open('output.txt', 'w') as f:
#     f.write(transportlist.date)

# print(transportlist)
# print(transportlist[0])
# print(transportlist[0].date)

for trans in transportlist:
    file.write('"' + str(trans.date) + '",')
    file.write('"' + str(trans.seq) + '",')
    file.write('"' + str(trans.departure) + '",')
    file.write('"' + str(trans.arrival) + '",')
    file.write('"' + str(trans.via) + '",')
    file.write('"' + str(trans.amount) + '",')

# ファイルクローズ
file.close()