#データベースとテーブルをインポートする
from database import session
from tables import stations
#引数を取得
import sys
args = sys.argv
from_name = str(args[1])
to_name = str(args[2])

##東京駅からの距離を取得する##
#引数に設定した駅名と同じ駅名をstationテーブルのname列から探し、
#同じレコード（行）のkilo列の値を取得する
from_kilo = session.query(stations.kilo).filter_by(name = from_name).all()
to_kilo = session.query(stations.kilo).filter_by(name = to_name).all()

from_kilo = str(from_kilo[0])   # リスト要素 (Decimal('x.xx'),)を取り出す
from_kilo = float(from_kilo[10:-4]) # 数値以外の部分をスライスして浮動小数点型に変換
to_kilo = str(to_kilo[0])      # (Decimal('x.xx'),)
to_kilo = float(to_kilo[10:-4]) # 数値以外の部分をスライスして浮動小数点型に変換

##計算して出力する##
#from_kiloとto_kiloの差を取り、小数第二位で四捨五入し絶対値を取る
print(abs(round(from_kilo - to_kilo,2)))