import sys
args = sys.argv

from database import session
from tables import Transport

# データを取得する
translist = session.query(Transport).all()

file_name = args[1]

t_file = open(file_name, mode="w", encoding="utf-8")

for transport in translist:
    print(f'"{transport.date}",'
          f'"{transport.seq}",'
          f'"{transport.departure}",'
          f'"{transport.arrival}",'
          f'"{transport.via}",'
          f'"{transport.amount}"')
    