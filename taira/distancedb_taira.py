from database import session
from table import Stations
import sys
args = sys.argv

input1 = args[1]
input2 = args[2]

a = session.query(Stations.kilo).filter_by(name = input1).first().kilo
b = session.query(Stations.kilo).filter_by(name = input2).first().kilo

sa = (float(a))-(float(b))
sa = round(sa,2)
if sa<0:
    print(-(float(sa)))
else:
    print(sa)