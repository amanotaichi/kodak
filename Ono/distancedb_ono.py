#データベースとテーブルをインポートする
from database import session
from tables import stations
#データを取得する
stationlist = session.query(stations).all()

import sys
args = sys.argv
from_station = str(args[1])
to_station = str(args[2])

