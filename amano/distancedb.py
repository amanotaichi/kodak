import sys
from databases import session
from tables import Stations

# 引数入力
args = sys.argv
stations_start = args[1]
stations_end = args[2]

# データベース全取得
# stationslist = session.query(Stations).all()

# データベース選択取得
stationslist_start = session.query(Stations).filter_by(name = stations_start).all()
stationslist_end = session.query(Stations).filter_by(name = stations_end).all()

# kiloのデータを取り出す
kilo_start = [station.kilo for station in stationslist_start]
kilo_end = [station.kilo for station in stationslist_end]

# Decimal型をfloat型に変換
kilo_start_float = [float(k) for k in kilo_start]
kilo_end_float = [float(k) for k in kilo_end]

# 2つの駅の東京からの距離を表示
print(kilo_start_float[0])
print(kilo_end_float[0])

# 2つの駅間の距離を計算
distance = abs(kilo_start_float[0] - kilo_end_float[0])

# 表示
print(distance)

# 入力駅の情報表示
# for stations in stationslist_start:
#     print(stations.seq, stations.name, stations.kilo)
# for stations in stationslist_end:
#     print(stations.seq, stations.name, stations.kilo)


