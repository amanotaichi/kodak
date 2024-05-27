import sys
from sqlalchemy import Column, String, Numeric, Integer, Date
from database import Base
from database import ENGINE

#テーブル：stationsの定義
class stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', String(20))
    kilo = Column('kilo', Numeric(6,2))
    
#テーブル：transportの定義
class Transport(Base): #クラス名は頭文字が大文字
    __tablename__ = 'transport'  #テーブル名は小文字
    Date = Column('Date', Date, primary_key = True) #datetimeモジュールのdate関数を使うために大文字
    seq = Column('seq', Integer, primary_key = True)
    departure = Column('departure', String(20))
    arrival = Column('arrival', String(20))
    via = Column('via', String(40))
    amount = Column('amount', Integer)
    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)