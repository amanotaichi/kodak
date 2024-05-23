import sys
from sqlalchemy import Column, String, Date, Integer, Numeric, DateTime, Float
from databases import Base
from databases import ENGINE

#テーブル：Stationsの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6, 2))

#テーブル：Transportの定義
class Transport(Base):
    __tablename__ = 'transport'
    date = Column('date', Date, primary_key = True)
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)

#テーブル：Lunchの定義
class Lunch(Base):
    __tablename__ = 'lunch'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    price = Column('price', Integer)
    cost = Column('cost', Float)

def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)