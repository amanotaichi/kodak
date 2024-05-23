import sys
args = sys.argv

depart = args[1]
arrive = args[2]

from database import session
from tables import Stations

stations = session.query(Stations.seq).filter_by(name=depart).all


"""
    distance = shinkansen[arrive] - shinkansen[depart]
    distance = round(distance, 2)
"""