from datetime import date
from database import session
from table import Transport2
import sys
args = sys.argv
try:

    input1 = args[1]
    input2 = int(args[2])
    input3 = args[3]
    input4 = args[4]
    input5 = args[5]
    input6 = int(args[6])


    transport2 = Transport2(
        date = input1,
        seq = input2,
        departure = input3,
        arrival = input4,
        via = input5,
        amount = input6
        )

    session.add(transport2)

    session .commit()
except  :
    print("エラーやで")




