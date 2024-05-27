import sys
args = sys.argv

from database import session
from tables import Transport


try:
    # 登録するデータの編集
    transport = Transport(
        date = args[1],
        seq = args[2],
        departure = args[3],    
        arrival = args[4], 
        via = args[5],
        amount = args[6]
    )

    # INSERT処理
    session.add(transport)

    # コミット
    session.commit()

    print("交通費精算テーブルにデータを登録しました")

except:
    print("error:交通費精算テーブルにデータを登録できませんでした")