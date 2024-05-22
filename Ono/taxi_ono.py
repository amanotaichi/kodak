import sys
args = sys.argv
num = int(args[1])

import math #mathモジュールをインポート

if num <= 1500: #1500以下の処理
    fare = 630
else: #1501以上の場合の処理
    #1500を引いた数を344で割り、それを切り上げた数を98かける
    fare = math.ceil((num - 1500) / 344) * 98 + 630

print(fare)