import sys
from sqlalchemy import Column, VARCHAR, DECIMAL
from database import Base
from database import ENGINE

#テーブル：stationsの定義
class stations(Base):
    __tablename__ = 'stations'
    seq = Column('seq', int, primary_key = True)
    name = Column('name', VARCHAR(20))
    kilo = Column('kilo', DECIMAL(6,2))
    
def main(args):
    """
    メイン関数
    """
    Base.metadata.create_all(bind=ENGINE)

if __name__ == "__main__":
        main(sys.argv)