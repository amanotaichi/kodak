from sqlalchemy import *   # 必要なモジュールを定義
from sqlalchemy.orm import *   # * 全て
from sqlalchemy.ext.declarative import declarative_base
import os

# mysqlのDBの設定
DATABASE = "mysql+pymysql://{user}:{password}@{host}/{database}?charset=utf8".format(**{
        "user": os.getenv("DB_USER", "root"), # getenv環境変数の定義
        "password": os.getenv("DB_PASSWORD", "mysql"),
        "host": os.getenv("DB_HOST", "localhost"),
        "database":os.getenv("DB_DATABASE", "ENSHU")
    })

ENGINE = create_engine(
    DATABASE,
    encoding = "utf-8",
    echo=True # True:実行のたびにSQLが出力
)

# Sessionの作成  接続セッションを保持するため
session = scoped_session(
  # ORM実行時の設定
    sessionmaker(
        autocommit = False,
        autoflush = False,
        bind = ENGINE
    )
)

# tables.pyで継承する
Base = declarative_base()
Base.query = session.query_property()