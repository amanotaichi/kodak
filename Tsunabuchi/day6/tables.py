import sys
from sqlalchemy import Column, Integer, VARCHAR, DECIMAL
from database import Base
from database import ENGINE

#テーブル：Stationsの定義
class Stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', Integer, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6,2))



def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)