import os
import sys
import qrcode

# 引数入力（テキストファイル名
args = sys.argv
name = args[1]

def make_qr(url, count):
    # パス指定
    path = os.path.join("output", str(count) + ".png")
    # QR生成
    img = qrcode.make(url)
    # 画像保存
    img.save(path)

try:
    count = 1
    # テキストファイルオープン
    with open(name) as f:
        line = f.readline()
        while line:
            print(count)
            print(line)
            make_qr(line, count)
            line = f.readline()
            count += 1
except Exception as e:
    print("error")
    print(e)
    sys.exit()
