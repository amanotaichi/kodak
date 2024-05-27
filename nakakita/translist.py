
from database import session
from tables import Transport

import sys
args = sys.argv

text_name = args[1]

trans_list = session.query(Transport).all() #queryで問い合わせ allで全件

t_file = open(text_name, mode="w", encoding="utf-8")

for transport in trans_list: #リスト全部繰り返し
    #print(f'["{transport.date}", "{transport.seq}", "{transport.departure}", "{transport.arrival}", "{transport.via}", "{transport.amount}"]\n')
    a = (f'["{transport.date}", "{transport.seq}", "{transport.departure}", "{transport.arrival}", "{transport.via}", "{transport.amount}"]\n')
    t_file.write(a)

t_file.close()

#for transport in trans_list: #リスト全部繰り返し
    #x = transport.date
    #a = [str(x), str(transport.seq), transport.departure, transport.arrival, transport.via, str(transport.amount)]
    #print(a)
