from datetime import date
from database import session
from table import Transport2

import sys 
args=sys.argv
input1 = args[1]

a = session.query(Transport2).all()


a_file = open(f"{input1}",mode="w",encoding="utf-8")

a_file.write(a_list)