import sys
args = sys.argv

from database import session
from tables import Stations

# データを取得する
input_station1 = session.query(Stations.kilo).filter_by(name = args[1]).first().kilo

input_station2 = session.query(Stations.kilo).filter_by(name = args[2]).first().kilo


#駅間の計算
distance = input_station2 - input_station1

#絶対値
distance = abs(distance)

# 出力（小数第二位まで）
print(str(round(distance,2)),end="")