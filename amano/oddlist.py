import sys

# リストの初期化
# 指定リスト
this_list = ["Kurita", "Tanaka", "Kaneda", "Noda", "Koyama", "Adachi", "Kuriyama", "Ohyama", "Kishida"]
# 出力リスト
next_list = []

# 出力用リストの作成
for i in range(len(this_list)):
    if i % 2 == 0:
        pass
    else:
        # print("'" + this_list[i] + "', ", end="")
        next_list.append(this_list[i])

# 表示
print(next_list, end="")