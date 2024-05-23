from decimal import Decimal,ROUND_HALF_UP
import sys
args = sys.argv

input1 = int(args[1])
input2 = int(args[2])

karaage = input1*760
curry = input2*850

genka_karaage = karaage*0.323 
genka_karaage = Decimal(str(genka_karaage)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

genka_curry = curry*0.284
genka_curry = Decimal(str(genka_curry)).quantize(Decimal("0"),rounding=ROUND_HALF_UP)

genka_sum = genka_curry + genka_karaage

sum = karaage + curry
arari = sum - genka_sum

print(f"売上高：{sum}、原価：{genka_sum}、粗利：{arari}")