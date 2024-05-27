#データベースとテーブルをインポートする
from database import session
from tables import Transport
from datetime import datetime, date
import pandas as pd
#引数を取得
import sys
args = sys.argv

# 数値型データ（YYYYMMDD）
int_type = int(args[1])
# 日付変換（YYYY-MM-DD HH:MM:SS)
datetime_type = pd.to_datetime(str(int_type))
# 日付変換（YYYY-MM-DD)
date_type     = date(datetime_type.year, datetime_type.month, datetime_type.day)

try:
    transport = Transport(
        Date = date_type,
        seq = int(args[2]),
        departure = str(args[3]),
        arrival= str(args[4]),
        via = str(args[5]),
        amount = int(args[6])
        )
    session.add(transport)
    session.commit()
except:
    print("error:交通費精算テーブルにデータを登録できませんでした")
else:
    print("交通費精算テーブルにデータを登録しました")