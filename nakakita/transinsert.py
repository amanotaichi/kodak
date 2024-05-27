from database import session
from tables import Transport

try:

    import sys
    args = sys.argv

    input_date = args[1]
    input_seq = int(args[2])
    input_departure = args[3]
    input_arrival = args[4]
    input_via = args[5]
    input_amount = int(args[6])

    transport = Transport(
        date = input_date,
        seq = input_seq,
        departure = input_departure,
        arrival = input_arrival,
        via = input_via,
        amount = input_amount
    )

    #INSERT処理
    session.add(transport)
    #コミット
    session.commit()

    print("交通費精算テーブルにデータを登録しました")

except:
    print("error:交通費精算テーブルにデータを登録できませんでした")
