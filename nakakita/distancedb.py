import sys
args = sys.argv

depart = args[1]
arrive = args[2]

from database import session
from tables import Stations

#テーブルからデータを取得
depart_station = session.query(Stations).filter_by(name=depart).first()
arrive_station = session.query(Stations).filter_by(name=arrive).first()

#距離を計算
distance = arrive_station.kilo - depart_station.kilo
distance = round(distance, 2)

print(distance)


#depart_name = session.query(Stations.name).filter_by(name=depart).first().name
#arrive_name = session.query(Stations.name).filter_by(name=arrive).first().name

#depart_kilo = session.query(Stations.kilo).filter_by(name=depart).first().kilo
#arrive_kilo = session.query(Stations.kilo).filter_by(name=arrive).first().kilo
